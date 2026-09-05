# Landing Page: "Autista di Camion 2026"

Landing page promozionale moderna, responsive e ottimizzata per la massima conversione e la condivisione sui social network (WhatsApp, Facebook, Telegram, LinkedIn, X).

## File del Progetto

```
landing-autista-camion-2026/
├── index.html              # Struttura semantica HTML5 con metatag Open Graph & Schema.org
├── css/
│   └── style.css           # Design system moderno, 3D book mockup, responsive breakpoints
├── js/
│   └── main.js             # Gestione accordion FAQ, sticky mobile bar, tracking clic Amazon
├── assets/
│   ├── cover.jpg           # Copertina originale ufficiale del libro Amazon
│   └── og-banner.jpg       # Banner Open Graph 1200x630 px generato per anteprime social
├── generate_og_image.py    # Script Python per rigenerare il banner OG con Pillow
└── README.md               # Guida alla configurazione e pubblicazione
```

---

## 1. Configurazione Rapida prima della Pubblicazione

Apri `index.html` e sostituisci il placeholder del dominio `https://tuodominio.it/` con l'indirizzo URL effettivo dove pubblicherai la pagina:

```html
<!-- Sostituisci https://tuodominio.it/ con il tuo URL effettivo -->
<link rel="canonical" href="https://tuo-sito.it/">
<meta property="og:url" content="https://tuo-sito.it/">
<meta property="og:image" content="https://tuo-sito.it/assets/og-banner.jpg">
<meta property="og:image:secure_url" content="https://tuo-sito.it/assets/og-banner.jpg">
<meta name="twitter:url" content="https://tuo-sito.it/">
<meta name="twitter:image" content="https://tuo-sito.it/assets/og-banner.jpg">
```

> **Nota**: Piattaforme come WhatsApp e Facebook richiedono un URL assoluto `https://...` per caricare l'immagine di anteprima `og:image`.

---

## 2. Come Pubblicarla Gratis in 2 Minuti

Puoi pubblicare questa cartella immediatamente su qualsiasi piattaforma gratuita per siti statici:

### Opzione A: Vercel / Netlify
1. Trascina la cartella `landing-autista-camion-2026` su [app.netlify.com/drop](https://app.netlify.com/drop) o collegala a un repository GitHub con [Vercel](https://vercel.com).
2. Otterrai subito un URL HTTPS gratuito (es. `https://autista-camion-2026.netlify.app/`).
3. Aggiorna i metatag di `index.html` con quel link.

### Opzione B: GitHub Pages
1. Crea un repository GitHub pubblico (es. `guida-autista-camion`).
2. Carica i file di questa cartella.
3. Vai in **Settings** > **Pages** e seleziona il branch `main`.

### Opzione C: Hosting proprio (Aruba, Siteground, cPanel, VPS, Apache/Nginx)
- Carica i file direttamente via FTP o SCP nella root `public_html` del tuo dominio.

---

## 3. Come Testare l'Anteprima Social (Open Graph)

Una volta pubblicato il link, puoi verificare come appare l'anteprima su WhatsApp e social con questi strumenti gratuiti:
- **OpenGraph.xyz**: [https://www.opengraph.xyz/](https://www.opengraph.xyz/)
- **Facebook Sharing Debugger**: [https://developers.facebook.com/tools/debug/](https://developers.facebook.com/tools/debug/)
- **LinkedIn Post Inspector**: [https://www.linkedin.com/post-inspector/](https://www.linkedin.com/post-inspector/)
- **Telegram Web / WhatsApp Web**: Incolla il link in una chat per vedere la generazione automatica della card con immagine e titolo.

---

## 4. Test Locale

Per testare la landing page in locale prima di pubblicarla:

```powershell
cd "C:\Users\pcù\.gemini\antigravity\scratch\landing-autista-camion-2026"
python -m http.server 8080
```

Apri il browser su [http://localhost:8080](http://localhost:8080).
