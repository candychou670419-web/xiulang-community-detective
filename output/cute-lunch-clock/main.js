/* ==========================================================================
   可愛數字電子鐘 - Electron 桌面應用程式主進程 (main.js)
   ========================================================================== */

const { app, BrowserWindow, Menu, Tray, nativeImage } = require('electron');
const path = require('path');

let mainWindow = null;
let tray = null;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1100,
        height: 780,
        minWidth: 800,
        minHeight: 600,
        title: '可愛數字電子鐘 - 國小午餐12:25提醒助手',
        icon: path.join(__dirname, 'icon.png'),
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            backgroundThrottling: false // 避免背景縮小後計時暫停
        },
        autoHideMenuBar: true,
        show: false
    });

    mainWindow.loadFile('index.html');

    // 視窗載入完成後顯示
    mainWindow.once('ready-to-show', () => {
        mainWindow.show();
    });

    // 視窗關閉保護 (最小化至系統托盤)
    mainWindow.on('close', (event) => {
        if (!app.isQuitting) {
            event.preventDefault();
            mainWindow.hide();
        }
        return false;
    });
}

function createTray() {
    // 建立托盤圖示與右鍵選單
    const icon = nativeImage.createFromNamedImage('clock');
    tray = new Tray(icon);
    tray.setToolTip('可愛數字電子鐘 (午餐12:25提醒)');

    const contextMenu = Menu.buildFromTemplate([
        { label: '⏰ 顯示主畫面', click: () => mainWindow.show() },
        { label: '🧪 測試 12:25 響鈴與煙火', click: () => {
            mainWindow.show();
            mainWindow.webContents.executeJavaScript('document.getElementById("testAlarmBtn").click()');
        }},
        { type: 'separator' },
        { label: '❌ 完全結束程式', click: () => {
            app.isQuitting = true;
            app.quit();
        }}
    ]);

    tray.setContextMenu(contextMenu);
    tray.on('double-click', () => {
        mainWindow.show();
    });
}

app.whenReady().then(() => {
    createWindow();
    createTray();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
