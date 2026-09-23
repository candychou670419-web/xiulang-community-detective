/* ==========================================================================
   可愛數字電子鐘 - JavaScript 邏輯引擎 (app.js)
   包含：數字鐘計時、12:25 觸發器、Web Audio 樂音合成器、Canvas 彩色煙火粒子系統
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // --- 狀態控制與變數定義 ---
    let alarmTime = localStorage.getItem('lunchClock_alarmTime') || '12:25';
    let musicVolume = parseFloat(localStorage.getItem('lunchClock_volume') || '0.8');
    let isMusicRepeat = localStorage.getItem('lunchClock_repeat') !== 'false';
    let speechMessage = localStorage.getItem('lunchClock_message') || '小朋友們，用餐要專心，多吃蔬菜身體棒棒喔！✨';

    let alarmTriggeredToday = false;
    let audioCtx = null;
    let isPlayingMusic = false;
    let musicTimerId = null;

    // DOM 元素選取
    const hoursText = document.getElementById('hoursText');
    const minutesText = document.getElementById('minutesText');
    const secondsText = document.getElementById('secondsText');
    const ampmText = document.getElementById('ampmText');
    const dateText = document.getElementById('dateText');
    const dayOfWeekText = document.getElementById('dayOfWeekText');
    const countdownTimer = document.getElementById('countdownTimer');
    const alarmTimeBadge = document.getElementById('alarmTimeBadge');
    const speechBubble = document.getElementById('speechBubble');

    const alarmModal = document.getElementById('alarmModal');
    const settingsModal = document.getElementById('settingsModal');

    const audioStatusBtn = document.getElementById('audioStatusBtn');
    const audioStatusIcon = document.getElementById('audioStatusIcon');
    const audioStatusText = document.getElementById('audioStatusText');
    const audioUnlockPrompt = document.getElementById('audioUnlockPrompt');
    const manualPlayMusicBtn = document.getElementById('manualPlayMusicBtn');

    const testAlarmBtn = document.getElementById('testAlarmBtn');
    const settingsBtn = document.getElementById('settingsBtn');
    const closeSettingsBtn = document.getElementById('closeSettingsBtn');
    const saveSettingsBtn = document.getElementById('saveSettingsBtn');
    const stopMusicBtn = document.getElementById('stopMusicBtn');
    const completeAlarmBtn = document.getElementById('completeAlarmBtn');
    const fullscreenBtn = document.getElementById('fullscreenBtn');

    const alarmTimeInput = document.getElementById('alarmTimeInput');
    const volumeRange = document.getElementById('volumeRange');
    const volumeVal = document.getElementById('volumeVal');
    const musicRepeatCheck = document.getElementById('musicRepeatCheck');
    const customMessageInput = document.getElementById('customMessageInput');

    // 初始化設定欄位預設值
    alarmTimeInput.value = alarmTime;
    alarmTimeBadge.textContent = alarmTime;
    volumeRange.value = Math.round(musicVolume * 100);
    volumeVal.textContent = Math.round(musicVolume * 100);
    musicRepeatCheck.checked = isMusicRepeat;
    customMessageInput.value = speechMessage;
    speechBubble.textContent = speechMessage;

    // 星期幾文字陣列
    const daysCN = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];

    // --- 音效解鎖與狀態監聽系統 (解決現代瀏覽器 Autoplay 阻擋問題) ---
    function updateAudioStatus() {
        if (!audioStatusBtn || !audioStatusIcon || !audioStatusText) return;
        if (!audioCtx || audioCtx.state === 'suspended') {
            audioStatusBtn.classList.add('needs-unlock');
            audioStatusIcon.textContent = '🔇';
            audioStatusText.textContent = '點此開啟音效';
        } else {
            audioStatusBtn.classList.remove('needs-unlock');
            audioStatusIcon.textContent = '🔊';
            audioStatusText.textContent = '音效已就緒';
        }
    }

    async function unlockAudioContext(silent = true) {
        try {
            if (!audioCtx) {
                const AudioContextClass = window.AudioContext || window.webkitAudioContext;
                audioCtx = new AudioContextClass();
            }
            if (audioCtx.state === 'suspended') {
                await audioCtx.resume();
            }
            // 播放 0.001 秒無聲音訊管線確保喚醒硬體輸出
            const buffer = audioCtx.createBuffer(1, 1, 22050);
            const source = audioCtx.createBufferSource();
            source.buffer = buffer;
            source.connect(audioCtx.destination);
            source.start(0);

            updateAudioStatus();

            if (!silent && audioCtx.state === 'running') {
                playTone(523.25, audioCtx.currentTime + 0.02, 0.12);
                playTone(659.25, audioCtx.currentTime + 0.15, 0.20);
            }
        } catch (err) {
            console.warn("unlockAudioContext error:", err);
        }
    }

    // 全局點擊/觸控/按鍵立即預先解鎖音效權限
    ['click', 'touchstart', 'pointerdown', 'keydown'].forEach(evt => {
        window.addEventListener(evt, () => {
            if (!audioCtx || audioCtx.state === 'suspended') {
                unlockAudioContext(true);
            }
        }, { passive: true });
    });

    updateAudioStatus();

    // --- 1. 時鐘與倒數計時核心邏輯 ---
    function updateClock() {
        const now = new Date();
        const year = now.getFullYear();
        const month = now.getMonth() + 1;
        const date = now.getDate();
        const day = daysCN[now.getDay()];

        let hours = now.getHours();
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');

        const isPM = hours >= 12;
        const ampmStr = isPM ? '下午' : '上午';

        // 12小時制顯示轉換
        let displayHours = hours % 12;
        displayHours = displayHours ? displayHours : 12; // 0點顯示為12
        const displayHoursStr = String(displayHours).padStart(2, '0');

        // 更新 UI
        dateText.textContent = `${year}年${month}月${date}日`;
        dayOfWeekText.textContent = day;
        hoursText.textContent = displayHoursStr;
        minutesText.textContent = minutes;
        secondsText.textContent = seconds;
        ampmText.textContent = ampmStr;

        // 計算距離提醒目標時間 (預設 12:25) 倒數
        calculateCountdown(now);

        // 比對時間觸發提醒 (以 24小時制 HH:mm 比對，避免因分頁節流跳過 00 秒)
        const currentHM = `${String(hours).padStart(2, '0')}:${minutes}`;
        if (currentHM === alarmTime && !alarmTriggeredToday) {
            triggerAlarmCelebration();
            alarmTriggeredToday = true;
        }

        // 當時間離開目標分鐘時，重置觸發狀態，確保明天同一時間能再次準時響鈴
        if (currentHM !== alarmTime && alarmTriggeredToday) {
            alarmTriggeredToday = false;
        }
    }

    function calculateCountdown(now) {
        const [targetH, targetM] = alarmTime.split(':').map(Number);
        let targetDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), targetH, targetM, 0);

        // 如果今日目標時間已過，設定為明日
        if (now > targetDate) {
            targetDate.setDate(targetDate.getDate() + 1);
        }

        const diffMs = targetDate - now;
        const diffSecTotal = Math.floor(diffMs / 1000);
        const diffMin = Math.floor(diffSecTotal / 60);
        const diffSec = diffSecTotal % 60;

        countdownTimer.textContent = `${String(diffMin).padStart(2, '0')}分 ${String(diffSec).padStart(2, '0')}秒`;
    }

    setInterval(updateClock, 1000);
    updateClock();

    // --- 2. Web Audio 多聲部歡樂音樂合成器 ---
    async function playCelebrationSong() {
        if (isPlayingMusic) stopCelebrationSong();

        await unlockAudioContext(true);

        if (!audioCtx || audioCtx.state !== 'running') {
            // 若瀏覽器政策阻止了定時背景自動發聲，顯示醒目的大按鈕讓老師一鍵播放
            if (audioUnlockPrompt) audioUnlockPrompt.style.display = 'flex';
            return;
        } else {
            if (audioUnlockPrompt) audioUnlockPrompt.style.display = 'none';
        }

        isPlayingMusic = true;

        // C大調歡慶樂譜 (音符與拍子)
        const notes = [
            // 第一句
            { note: 523.25, duration: 0.25 }, // C5
            { note: 587.33, duration: 0.25 }, // D5
            { note: 659.25, duration: 0.25 }, // E5
            { note: 698.46, duration: 0.25 }, // F5
            { note: 783.99, duration: 0.5 },  // G5
            { note: 783.99, duration: 0.5 },  // G5
            
            // 第二句
            { note: 880.00, duration: 0.25 }, // A5
            { note: 880.00, duration: 0.25 }, // A5
            { note: 880.00, duration: 0.25 }, // A5
            { note: 880.00, duration: 0.25 }, // A5
            { note: 783.99, duration: 0.75 }, // G5

            // 第三句 (歡快旋律高潮)
            { note: 659.25, duration: 0.25 }, // E5
            { note: 659.25, duration: 0.25 }, // E5
            { note: 659.25, duration: 0.5 },  // E5
            { note: 587.33, duration: 0.25 }, // D5
            { note: 587.33, duration: 0.25 }, // D5
            { note: 587.33, duration: 0.5 },  // D5
            { note: 523.25, duration: 0.75 }  // C5
        ];

        let currentTime = audioCtx.currentTime + 0.08;
        const totalDuration = notes.reduce((sum, item) => sum + item.duration, 0);

        notes.forEach(item => {
            playTone(item.note, currentTime, item.duration * 0.9);
            currentTime += item.duration;
        });

        // 循環播放控制
        if (isMusicRepeat) {
            musicTimerId = setTimeout(() => {
                if (isPlayingMusic) {
                    playCelebrationSong();
                }
            }, totalDuration * 1000 + 350);
        }
    }

    function playTone(freq, startTime, duration) {
        if (!audioCtx || audioCtx.state !== 'running' || musicVolume <= 0) return;

        try {
            const osc = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();

            osc.type = 'triangle'; // 柔和童趣聲音
            osc.frequency.setValueAtTime(freq, startTime);

            const safeStart = Math.max(startTime, audioCtx.currentTime + 0.005);
            const safeEnd = safeStart + duration;

            // 使用平滑線性 Ramp 防止指數 Ramp 從 0 開始拋出 DOMException 錯誤
            gainNode.gain.setValueAtTime(0.0001, safeStart);
            gainNode.gain.linearRampToValueAtTime(musicVolume * 0.45, safeStart + 0.04);
            gainNode.gain.linearRampToValueAtTime(0.0001, safeEnd);

            osc.connect(gainNode);
            gainNode.connect(audioCtx.destination);

            osc.start(safeStart);
            osc.stop(safeEnd + 0.02);
        } catch (e) {
            console.warn("playTone error:", e);
        }
    }

    function stopCelebrationSong() {
        isPlayingMusic = false;
        if (musicTimerId) {
            clearTimeout(musicTimerId);
            musicTimerId = null;
        }
    }

    // --- 3. HTML5 Canvas 全螢幕璀璨煙火粒子系統 ---
    const canvas = document.getElementById('fireworksCanvas');
    const ctx = canvas.getContext('2d');
    let particles = [];
    let fireworksAnimId = null;
    let isFireworksRunning = false;

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    class Particle {
        constructor(x, y, color, isSparkle = false, isRibbon = false) {
            this.x = x;
            this.y = y;
            this.color = color;
            this.isSparkle = isSparkle;
            this.isRibbon = isRibbon;

            const angle = Math.random() * Math.PI * 2;
            const speed = isRibbon ? Math.random() * 3 + 1 : (Math.random() * 9 + 3);
            
            this.vx = Math.cos(angle) * speed;
            this.vy = Math.sin(angle) * speed - (isRibbon ? 1 : 0);
            this.alpha = 1;
            this.decay = isRibbon ? (Math.random() * 0.008 + 0.005) : (Math.random() * 0.018 + 0.012);
            this.gravity = isRibbon ? 0.06 : 0.15;
            this.size = isRibbon ? (Math.random() * 6 + 4) : (Math.random() * 5 + 3);
            this.rotation = Math.random() * Math.PI * 2;
            this.rotSpeed = (Math.random() - 0.5) * 0.2;
        }

        update() {
            this.vx *= 0.96;
            this.vy *= 0.96;
            this.vy += this.gravity;
            this.x += this.vx;
            this.y += this.vy;
            this.alpha -= this.decay;
            this.rotation += this.rotSpeed;
        }

        draw() {
            ctx.save();
            ctx.globalAlpha = Math.max(0, this.alpha);
            ctx.shadowBlur = 15;
            ctx.shadowColor = this.color;
            ctx.fillStyle = this.color;

            if (this.isRibbon) {
                ctx.translate(this.x, this.y);
                ctx.rotate(this.rotation);
                ctx.fillRect(-this.size / 2, -this.size / 4, this.size, this.size / 2);
            } else {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
            ctx.restore();
        }
    }

    function createFireworkExplosion(x, y) {
        const vibrantColors = [
            '#FF0055', '#FFCC00', '#00FFCC', '#FF00FF', 
            '#00E5FF', '#76FF03', '#FF6D00', '#D500F9', '#FFFFFF'
        ];
        const baseColor = vibrantColors[Math.floor(Math.random() * vibrantColors.length)];

        // 主環狀爆炸 (100 顆發光粒子)
        for (let i = 0; i < 100; i++) {
            particles.push(new Particle(x, y, baseColor));
        }

        // 副發光閃爍小星花 (40 顆)
        const secondaryColor = vibrantColors[Math.floor(Math.random() * vibrantColors.length)];
        for (let i = 0; i < 40; i++) {
            particles.push(new Particle(x, y, secondaryColor, true));
        }

        // 彩色飄落彩帶 (20 條)
        for (let i = 0; i < 20; i++) {
            const ribbonColor = vibrantColors[Math.floor(Math.random() * vibrantColors.length)];
            particles.push(new Particle(x, y, ribbonColor, false, true));
        }
    }

    function startFireworksAnimation() {
        isFireworksRunning = true;
        particles = [];
        
        let launchCounter = 0;
        const launchInterval = setInterval(() => {
            if (!isFireworksRunning) {
                clearInterval(launchInterval);
                return;
            }
            // 隨機雙重連環噴發
            const x1 = Math.random() * (canvas.width * 0.8) + (canvas.width * 0.1);
            const y1 = Math.random() * (canvas.height * 0.45) + (canvas.height * 0.1);
            createFireworkExplosion(x1, y1);

            if (Math.random() > 0.4) {
                const x2 = Math.random() * (canvas.width * 0.8) + (canvas.width * 0.1);
                const y2 = Math.random() * (canvas.height * 0.45) + (canvas.height * 0.1);
                createFireworkExplosion(x2, y2);
            }
            
            launchCounter++;
            if (launchCounter >= 40 && !alarmModal.classList.contains('active')) {
                clearInterval(launchInterval);
            }
        }, 200);

        function animate() {
            if (!isFireworksRunning && particles.length === 0) {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                cancelAnimationFrame(fireworksAnimId);
                return;
            }

            ctx.globalCompositeOperation = 'source-over';
            ctx.fillStyle = 'rgba(15, 23, 42, 0.25)'; // 微暗底色襯托燦爛煙火
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.globalCompositeOperation = 'lighter'; // 光度疊加模式，煙火極致發光

            for (let i = particles.length - 1; i >= 0; i--) {
                particles[i].update();
                particles[i].draw();
                if (particles[i].alpha <= 0) {
                    particles.splice(i, 1);
                }
            }

            fireworksAnimId = requestAnimationFrame(animate);
        }

        animate();
    }

    function stopFireworksAnimation() {
        isFireworksRunning = false;
        particles = [];
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    // --- 4. 提醒與彈窗觸發控制 ---
    async function triggerAlarmCelebration() {
        alarmModal.classList.add('active');
        startFireworksAnimation();
        await playCelebrationSong();

        // 重置核取方塊
        document.querySelectorAll('.checklist-grid input[type="checkbox"]').forEach(cb => cb.checked = false);
    }

    function dismissAlarmCelebration() {
        alarmModal.classList.remove('active');
        stopCelebrationSong();
        stopFireworksAnimation();
    }

    // --- 5. 事件監聽與互動控制 ---
    // 音效狀態檢測按鈕 (點擊播放雙音測試並解鎖)
    if (audioStatusBtn) {
        audioStatusBtn.addEventListener('click', () => {
            unlockAudioContext(false);
        });
    }

    // 彈窗手動解鎖播放音樂大按鈕
    if (manualPlayMusicBtn) {
        manualPlayMusicBtn.addEventListener('click', async () => {
            await unlockAudioContext(true);
            playCelebrationSong();
        });
    }

    // 當彈窗出現時，若音樂受阻，點擊彈窗任一處或核取項目自動補播音樂
    alarmModal.addEventListener('click', (e) => {
        if (!isPlayingMusic && !e.target.closest('#stopMusicBtn') && !e.target.closest('#completeAlarmBtn')) {
            unlockAudioContext(true).then(() => {
                if (!isPlayingMusic && alarmModal.classList.contains('active')) {
                    playCelebrationSong();
                }
            });
        }
    });

    // 測試提醒按鈕
    testAlarmBtn.addEventListener('click', () => {
        triggerAlarmCelebration();
    });

    // 暫停音樂
    stopMusicBtn.addEventListener('click', () => {
        stopCelebrationSong();
    });

    // 完成提醒
    completeAlarmBtn.addEventListener('click', () => {
        dismissAlarmCelebration();
    });

    // 主題切換
    document.querySelectorAll('.theme-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.theme-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const selectedTheme = btn.getAttribute('data-theme');
            document.body.className = selectedTheme;
        });
    });

    // 全螢幕切換
    fullscreenBtn.addEventListener('click', () => {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen().catch(err => {
                console.log(`全螢幕切換失敗: ${err.message}`);
            });
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            }
        }
    });

    // 設定視窗開關與儲存
    settingsBtn.addEventListener('click', () => {
        settingsModal.classList.add('active');
    });

    closeSettingsBtn.addEventListener('click', () => {
        settingsModal.classList.remove('active');
    });

    volumeRange.addEventListener('input', (e) => {
        volumeVal.textContent = e.target.value;
    });

    saveSettingsBtn.addEventListener('click', () => {
        alarmTime = alarmTimeInput.value || '12:25';
        musicVolume = parseInt(volumeRange.value, 10) / 100;
        isMusicRepeat = musicRepeatCheck.checked;
        speechMessage = customMessageInput.value;

        localStorage.setItem('lunchClock_alarmTime', alarmTime);
        localStorage.setItem('lunchClock_volume', musicVolume);
        localStorage.setItem('lunchClock_repeat', isMusicRepeat);
        localStorage.setItem('lunchClock_message', speechMessage);

        alarmTimeBadge.textContent = alarmTime;
        speechBubble.textContent = speechMessage;
        settingsModal.classList.remove('active');
        
        // 重新計算倒數
        updateClock();
    });
});
