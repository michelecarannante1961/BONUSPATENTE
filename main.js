/**
 * Autista di Camion 2026 - Interactive Scripts
 * Lightweight, dependency-free vanilla JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
  initFaqAccordion();
  initStickyMobileBar();
  initAmazonClickTracking();
  initCurrentYear();
});

/**
 * FAQ Accordion with smooth transitions and ARIA accessibility
 */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (!questionBtn || !answer) return;

    questionBtn.addEventListener('click', () => {
      const isOpen = item.classList.contains('active');

      // Close all other open items
      faqItems.forEach(otherItem => {
        if (otherItem !== item && otherItem.classList.contains('active')) {
          otherItem.classList.remove('active');
          const otherBtn = otherItem.querySelector('.faq-question');
          const otherAns = otherItem.querySelector('.faq-answer');
          if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          if (otherAns) otherAns.style.maxHeight = null;
        }
      });

      // Toggle current item
      if (isOpen) {
        item.classList.remove('active');
        questionBtn.setAttribute('aria-expanded', 'false');
        answer.style.maxHeight = null;
      } else {
        item.classList.add('active');
        questionBtn.setAttribute('aria-expanded', 'true');
        answer.style.maxHeight = answer.scrollHeight + 25 + 'px';
      }
    });
  });
}

/**
 * Sticky Mobile Purchase Bar
 * Displays after user scrolls past the hero section (approx 450px)
 */
function initStickyMobileBar() {
  const stickyBar = document.getElementById('stickyBar');
  if (!stickyBar) return;

  const scrollThreshold = 450;
  let ticking = false;

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        if (window.scrollY > scrollThreshold) {
          stickyBar.classList.add('visible');
        } else {
          stickyBar.classList.remove('visible');
        }
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
}

/**
 * Outbound Click Tracking Helper for Amazon CTA Links
 * Ready for Google Tag Manager, Google Analytics 4, or Meta Pixel
 */
function initAmazonClickTracking() {
  const amazonLinks = document.querySelectorAll('a[href*="amazon"], a[href*="amzn.eu"]');

  amazonLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      // If Google Analytics 4 is present
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'click_amazon_buy', {
          event_category: 'outbound',
          event_label: link.href,
          transport_type: 'beacon'
        });
      }

      // If Facebook Pixel is present
      if (typeof window.fbq === 'function') {
        window.fbq('track', 'InitiateCheckout', {
          content_name: 'Autista di Camion 2026',
          currency: 'EUR',
          value: 6.99
        });
      }
    });
  });
}

/**
 * Update Copyright Year Dynamically
 */
function initCurrentYear() {
  const yearSpan = document.getElementById('currentYear');
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }
}
