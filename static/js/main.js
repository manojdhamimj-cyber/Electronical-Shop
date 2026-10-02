// Electronical Enterprise Vanilla JavaScript
document.addEventListener('DOMContentLoaded', () => {
  // Notification Enable / Disable Switcher (Syncs PC & Mobile)
  const notifToggle = document.getElementById('notifToggle');
  const notifIcon = document.getElementById('notifIcon');
  const notifText = document.getElementById('notifText');
  const drawerNotifToggle = document.getElementById('drawerNotifToggle');
  const drawerNotifIcon = document.getElementById('drawerNotifIcon');
  const drawerNotifText = document.getElementById('drawerNotifText');
  const notifBanner = document.getElementById('notifBanner');

  function updateNotifUI(muted) {
    if (notifBanner) {
      notifBanner.style.display = muted ? 'none' : 'block';
    }
    
    // Navbar button
    if (notifToggle) {
      notifToggle.classList.toggle('muted', muted);
      if (notifIcon) notifIcon.textContent = muted ? '🔕' : '🔔';
      if (notifText) notifText.textContent = muted ? 'Disabled' : 'Enabled';
    }

    // Mobile Drawer button
    if (drawerNotifToggle) {
      drawerNotifToggle.classList.toggle('muted', muted);
      if (drawerNotifIcon) drawerNotifIcon.textContent = muted ? '🔕' : '🔔';
      if (drawerNotifText) drawerNotifText.textContent = muted ? 'Disabled' : 'Enabled';
    }
  }

  const isMutedInitially = localStorage.getItem('electronical_notif_muted') === 'true';
  updateNotifUI(isMutedInitially);

  function toggleNotificationState() {
    const currentlyMuted = localStorage.getItem('electronical_notif_muted') === 'true';
    const newMutedState = !currentlyMuted;
    localStorage.setItem('electronical_notif_muted', String(newMutedState));
    updateNotifUI(newMutedState);
    showToast(newMutedState ? '🔕 Offers & Notifications Disabled' : '🔔 Notifications Enabled!');
  }

  if (notifToggle) notifToggle.addEventListener('click', toggleNotificationState);
  if (drawerNotifToggle) drawerNotifToggle.addEventListener('click', toggleNotificationState);

  // Mobile Menu Drawer (Right-to-Left Slide-in)
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const mobileDrawerOverlay = document.getElementById('mobileDrawerOverlay');
  const mobileDrawerClose = document.getElementById('mobileDrawerClose');

  function openMobileMenu() {
    if (mobileDrawer) mobileDrawer.classList.add('open');
    if (mobileDrawerOverlay) mobileDrawerOverlay.classList.add('open');
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
  }

  function closeMobileMenu() {
    if (mobileDrawer) mobileDrawer.classList.remove('open');
    if (mobileDrawerOverlay) mobileDrawerOverlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      openMobileMenu();
    });
  }

  if (mobileDrawerClose) {
    mobileDrawerClose.addEventListener('click', closeMobileMenu);
  }

  if (mobileDrawerOverlay) {
    mobileDrawerOverlay.addEventListener('click', closeMobileMenu);
  }

  // Close on escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMobileMenu();
  });

  // Flash Sale Countdown Timer
  const timerElements = {
    hours: document.getElementById('timerHours'),
    minutes: document.getElementById('timerMinutes'),
    seconds: document.getElementById('timerSeconds')
  };

  if (timerElements.hours) {
    let timeLeft = 3600 * 14 + 1800; // 14 hours 30 mins
    setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
        const h = Math.floor(timeLeft / 3600);
        const m = Math.floor((timeLeft % 3600) / 60);
        const s = timeLeft % 60;
        timerElements.hours.textContent = String(h).padStart(2, '0');
        timerElements.minutes.textContent = String(m).padStart(2, '0');
        timerElements.seconds.textContent = String(s).padStart(2, '0');
      }
    }, 1000);
  }

  // Wishlist Toggle via AJAX
  document.querySelectorAll('.wishlist-btn').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.preventDefault();
      const productId = btn.getAttribute('data-product-id');
      try {
        const response = await fetch(`/wishlist/toggle/${productId}/`, {
          headers: { 'X-Requested-With': 'XMLHttpRequest' }
        });
        const data = await response.json();
        if (data.status === 'success') {
          btn.classList.toggle('active', data.added);
          const counter = document.getElementById('wishlistCounter');
          if (counter) counter.textContent = data.wishlist_count;
          showToast(data.added ? 'Added to wishlist!' : 'Removed from wishlist');
        }
      } catch (err) {
        console.error('Wishlist error', err);
      }
    });
  });

  // Simple Toast UI
  function showToast(message) {
    let toast = document.getElementById('toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'toast';
      toast.style.cssText = `
        position: fixed;
        bottom: 24px;
        right: 24px;
        background: #00d4ff;
        color: #050812;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 700;
        z-index: 9999;
        box-shadow: 0 10px 25px rgba(0,212,255,0.4);
        transition: all 0.3s ease;
      `;
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.style.opacity = '1';
    toast.style.transform = 'translateY(0)';
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
    }, 2500);
  }

  // PWA Service Worker Registration & Installation Prompt Handler
  let deferredPrompt = null;
  const installAppBtn = document.getElementById('installAppBtn');
  const drawerInstallBtn = document.getElementById('drawerInstallBtn');

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    if (installAppBtn) installAppBtn.style.display = 'inline-flex';
    if (drawerInstallBtn) drawerInstallBtn.style.display = 'inline-flex';
  });

  async function triggerAppInstall() {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      if (outcome === 'accepted') {
        showToast('🚀 Installing Gada Electronics App...');
      }
      deferredPrompt = null;
    } else {
      // Browser already installed or manual instructions for iOS / desktop
      showToast('💡 Tip: Tap "Add to Home Screen" or install via your browser menu');
    }
  }

  if (installAppBtn) installAppBtn.addEventListener('click', triggerAppInstall);
  if (drawerInstallBtn) drawerInstallBtn.addEventListener('click', triggerAppInstall);

  window.addEventListener('appinstalled', () => {
    showToast('🎉 Gada Electronics App installed successfully!');
    deferredPrompt = null;
  });

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/static/js/sw.js').catch(err => {
      console.log('SW registration note:', err);
    });
  }
});
