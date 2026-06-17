<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="QDcbcexQfj25IwMRhbQOaA5ce1MW5ZmVwEPIotEM">

    <title>Nhà ở cho thuê | Vinhomes Online</title>

    <meta name="description" content="Căn hộ, nhà phố, biệt thự cho thuê tại các đại đô thị.">


<meta name="robots" content="index,follow">
<link rel="canonical" href="https://vinhomesonline.vn/leasing/estate-for-rent">


<meta property="og:type" content="website">
<meta property="og:title" content="Nhà ở cho thuê">
<meta property="og:description" content="Căn hộ, nhà phố, biệt thự cho thuê tại các đại đô thị.">
<meta property="og:url" content="http://vinhomesonline.vn/leasing/estate-for-rent">
<meta property="og:site_name" content="Vinhomes Online">
<meta property="og:locale" content="vi_VN">
    

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Nhà ở cho thuê">
<meta name="twitter:description" content="Căn hộ, nhà phố, biệt thự cho thuê tại các đại đô thị.">
    


    <style>[x-cloak]{display:none !important;}</style>
    <link rel="preload" as="style" href="https://vinhomesonline.vn/build/assets/app-DbihfOi2.css" /><link rel="modulepreload" as="script" href="https://vinhomesonline.vn/build/assets/app-D5Qkzqvf.js" /><link rel="stylesheet" href="https://vinhomesonline.vn/build/assets/app-DbihfOi2.css" /><script type="module" src="https://vinhomesonline.vn/build/assets/app-D5Qkzqvf.js"></script><script id="browser-logger-active">
(function() {
    const ENDPOINT = 'http://vinhomesonline.vn/_boost/browser-logs';
    const logQueue = [];
    let flushTimeout = null;

    console.log('🔍 Browser logger active (MCP server detected). Posting to: ' + ENDPOINT);

    // Store original console methods
    const originalConsole = {
        log: console.log,
        info: console.info,
        error: console.error,
        warn: console.warn,
        table: console.table
    };

    // Helper to safely stringify values
    function safeStringify(obj) {
        const seen = new WeakSet();
        return JSON.stringify(obj, (key, value) => {
            if (typeof value === 'object' && value !== null) {
                if (seen.has(value)) return '[Circular]';
                seen.add(value);
            }
            if (value instanceof Error) {
                return {
                    name: value.name,
                    message: value.message,
                    stack: value.stack
                };
            }
            return value;
        });
    }

    // Batch and send logs
    function flushLogs() {
        if (logQueue.length === 0) return;

        const batch = logQueue.splice(0, logQueue.length);

        fetch(ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({ logs: batch })
        }).catch(err => {
            // Silently fail to avoid infinite loops
            originalConsole.error('Failed to send logs:', err);
        });
    }

    // Debounced flush (100ms)
    function scheduleFlush() {
        if (flushTimeout) clearTimeout(flushTimeout);
        flushTimeout = setTimeout(flushLogs, 100);
    }

    // Intercept console methods
    ['log', 'info', 'error', 'warn', 'table'].forEach(method => {
        console[method] = function(...args) {
            // Call original method
            originalConsole[method].apply(console, args);

            // Capture log data
            try {
                logQueue.push({
                    type: method,
                    timestamp: new Date().toISOString(),
                    data: args.map(arg => {
                        try {
                            return typeof arg === 'object' ? JSON.parse(safeStringify(arg)) : arg;
                        } catch (e) {
                            return String(arg);
                        }
                    }),
                    url: window.location.href,
                    userAgent: navigator.userAgent
                });

                scheduleFlush();
            } catch (e) {
                // Fail silently
            }
        };
    });

    // Global error handlers for uncaught errors
    const originalOnError = window.onerror;
    window.onerror = function boostErrorHandler(errorMsg, url, lineNumber, colNumber, error) {
        try {
            logQueue.push({
                type: 'uncaught_error',
                timestamp: new Date().toISOString(),
                data: [{
                    message: errorMsg,
                    filename: url,
                    lineno: lineNumber,
                    colno: colNumber,
                    error: error ? {
                        name: error.name,
                        message: error.message,
                        stack: error.stack
                    } : null
                }],
                url: window.location.href,
                userAgent: navigator.userAgent
            });

            scheduleFlush();
        } catch (e) {
            // Fail silently
        }

        // Call original handler if it exists
        if (originalOnError && typeof originalOnError === 'function') {
            return originalOnError(errorMsg, url, lineNumber, colNumber, error);
        }

        // Let the error continue to propagate
        return false;
    }
    window.addEventListener('error', (event) => {
        try {
            logQueue.push({
                type: 'window_error',
                timestamp: new Date().toISOString(),
                data: [{
                    message: event.message,
                    filename: event.filename,
                    lineno: event.lineno,
                    colno: event.colno,
                    error: event.error ? {
                        name: event.error.name,
                        message: event.error.message,
                        stack: event.error.stack
                    } : null
                }],
                url: window.location.href,
                userAgent: navigator.userAgent
            });

            scheduleFlush();
        } catch (e) {
            // Fail silently
        }

        // Let the error continue to propagate
        return false;
    });
    window.addEventListener('unhandledrejection', (event) => {
        try {
            logQueue.push({
                type: 'error',
                timestamp: new Date().toISOString(),
                data: [{
                    message: 'Unhandled Promise Rejection',
                    reason: event.reason instanceof Error ? {
                        name: event.reason.name,
                        message: event.reason.message,
                        stack: event.reason.stack
                    } : event.reason
                }],
                url: window.location.href,
                userAgent: navigator.userAgent
            });

            scheduleFlush();
        } catch (e) {
            // Fail silently
        }

        // Let the rejection continue to propagate
        return false;
    });

    // Flush on page unload
    window.addEventListener('beforeunload', () => {
        if (logQueue.length > 0) {
            navigator.sendBeacon(ENDPOINT, JSON.stringify({ logs: logQueue }));
        }
    });
})();
</script>
</head>
<body class="min-h-screen flex flex-col bg-surface text-ink antialiased">
    <header class="sticky top-0 z-50 shadow-sm" x-data="{ mobileOpen: false }">
    
    <div class="hidden lg:block bg-primary-darker text-white">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="flex h-9 items-center justify-between text-xs">
                <div class="flex items-center gap-5">
                    <a href="tel:19001234" class="flex items-center gap-1.5 text-white/80 hover:text-white transition-colors">
                        <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z"/>
                        </svg>
                        Hotline: 1900 1234
                    </a>
                    <span class="text-white/30">|</span>
                    <span class="text-white/70">Thứ 2 – Chủ nhật: 8:00 – 21:00</span>
                </div>
                <div class="flex items-center gap-4 text-white/70">
                    <a href="/huong-dan" class="hover:text-white transition-colors">Hướng dẫn</a>
                    <a href="/lien-he" class="hover:text-white transition-colors">Liên hệ</a>
                                            <span class="text-white/50">|</span>
                        <a href="https://vinhomesonline.vn/login" class="hover:text-white transition-colors">Đăng nhập</a>
                                    </div>
            </div>
        </div>
    </div>

    
    <div class="bg-white border-b border-line">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="flex h-[60px] items-center justify-between gap-4">
                
                <a href="/" class="flex items-center gap-2.5 shrink-0">
                    <span class="inline-flex h-8 w-8 items-center justify-center rounded-lg bg-primary text-white font-extrabold text-sm">V</span>
                    <span class="font-display text-[17px] font-extrabold uppercase tracking-tight text-primary leading-none">
                        Vinhomes Online
                    </span>
                </a>

                
                <nav class="hidden lg:flex items-center gap-1" aria-label="Điều hướng chính">
                        <div class="relative" x-data="{ open: false }"
                 @mouseenter="open = true" @mouseleave="open = false">
                <button type="button"
                        @focus="open = true"
                        :aria-expanded="open.toString()"
                        class="flex items-center gap-1 px-3 py-2 text-sm font-semibold text-ink hover:text-primary transition-colors duration-150">
                    Mua
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                    </svg>
                </button>
                <div x-show="open" x-cloak x-transition.opacity
                     class="absolute left-0 top-full pt-2 z-40">
                    <div class="bg-surface rounded-lg shadow-overlay border border-line p-5 grid gap-6"
                         style="grid-template-columns: repeat(2, minmax(180px, 1fr));">
                                                    <div>
                                <p class="text-xs font-bold uppercase tracking-wide text-muted mb-2">Theo loại giao dịch</p>
                                <ul class="space-y-1">
                                                                            <li>
                                            <a href="/so-cap"
                                               class="block py-1 text-sm text-ink hover:text-primary transition-colors duration-150">
                                                Bán sơ cấp
                                            </a>
                                        </li>
                                                                            <li>
                                            <a href="/thu-cap"
                                               class="block py-1 text-sm text-ink hover:text-primary transition-colors duration-150">
                                                Bán thứ cấp
                                            </a>
                                        </li>
                                                                    </ul>
                            </div>
                                                    <div>
                                <p class="text-xs font-bold uppercase tracking-wide text-muted mb-2">Khám phá</p>
                                <ul class="space-y-1">
                                                                            <li>
                                            <a href="/du-an"
                                               class="block py-1 text-sm text-ink hover:text-primary transition-colors duration-150">
                                                Tất cả dự án
                                            </a>
                                        </li>
                                                                            <li>
                                            <a href="/du-an?featured=1"
                                               class="block py-1 text-sm text-ink hover:text-primary transition-colors duration-150">
                                                Dự án nổi bật
                                            </a>
                                        </li>
                                                                    </ul>
                            </div>
                                            </div>
                </div>
            </div>
                                <div class="relative" x-data="{ open: false }"
                 @mouseenter="open = true" @mouseleave="open = false">
                <button type="button"
                        @focus="open = true"
                        :aria-expanded="open.toString()"
                        class="flex items-center gap-1 px-3 py-2 text-sm font-semibold text-ink hover:text-primary transition-colors duration-150">
                    Thuê
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                    </svg>
                </button>
                <div x-show="open" x-cloak x-transition.opacity
                     class="absolute left-0 top-full pt-2 z-40">
                    <div class="bg-surface rounded-lg shadow-overlay border border-line p-5 grid gap-6"
                         style="grid-template-columns: repeat(1, minmax(180px, 1fr));">
                                                    <div>
                                <p class="text-xs font-bold uppercase tracking-wide text-muted mb-2">Cho thuê</p>
                                <ul class="space-y-1">
                                                                            <li>
                                            <a href="/leasing/estate-for-rent"
                                               class="block py-1 text-sm text-ink hover:text-primary transition-colors duration-150">
                                                Nhà ở cho thuê
                                            </a>
                                        </li>
                                                                            <li>
                                            <a href="/commercial-leasing"
                                               class="block py-1 text-sm text-ink hover:text-primary transition-colors duration-150">
                                                Mặt bằng thương mại
                                            </a>
                                        </li>
                                                                    </ul>
                            </div>
                                            </div>
                </div>
            </div>
                                <a href="/du-an"
               class="px-3 py-2 text-sm font-semibold text-ink hover:text-primary transition-colors duration-150">
                Dự án
            </a>
                                <a href="/blog"
               class="px-3 py-2 text-sm font-semibold text-ink hover:text-primary transition-colors duration-150">
                Tin tức
            </a>
                                <a href="/lien-he"
               class="px-3 py-2 text-sm font-semibold text-ink hover:text-primary transition-colors duration-150">
                Liên hệ
            </a>
            </nav>

                
                <div class="hidden lg:flex items-center gap-2.5">
                                            <a href="https://vinhomesonline.vn/login" class="px-3 py-2 text-sm font-semibold text-ink hover:text-primary transition-colors duration-150">
                            Đăng nhập
                        </a>
                                                                <a href="https://vinhomesonline.vn/dang-ky-dai-ly" class="inline-flex items-center gap-1.5 rounded-lg bg-accent-cta px-4 py-2 text-sm font-bold text-white hover:opacity-90 transition-opacity duration-150 shadow-sm">
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"/>
                            </svg>
                            Đăng tin
                        </a>
                                    </div>

                
                <button type="button" class="lg:hidden p-2 text-ink rounded-md hover:bg-line/40 transition"
                        @click="mobileOpen = !mobileOpen"
                        :aria-expanded="mobileOpen.toString()"
                        aria-label="Menu">
                    <svg x-show="!mobileOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                    </svg>
                    <svg x-show="mobileOpen" x-cloak class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                    </svg>
                </button>
            </div>
        </div>
    </div>

    
    <div x-show="mobileOpen" x-cloak
         x-transition:enter="transition ease-out duration-200"
         x-transition:enter-start="opacity-0 -translate-y-1"
         x-transition:enter-end="opacity-100 translate-y-0"
         x-transition:leave="transition ease-in duration-150"
         x-transition:leave-start="opacity-100"
         x-transition:leave-end="opacity-0"
         class="lg:hidden border-t border-line bg-white shadow-raised">
        
        <div class="px-4 py-3 bg-primary-darker/5 border-b border-line">
            <a href="tel:19001234" class="flex items-center gap-2 text-sm font-bold text-primary">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z"/>
                </svg>
                Hotline: 1900 1234
            </a>
        </div>
        <nav class="px-4 py-3 space-y-0.5" aria-label="Điều hướng di động">
                                                <div x-data="{ sub: false }" class="border-b border-line/50">
                        <button type="button" @click="sub = !sub"
                                class="flex w-full items-center justify-between py-2.5 text-sm font-semibold text-ink">
                            Mua
                            <svg class="w-4 h-4 text-muted transition-transform duration-150" :class="sub && 'rotate-180'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                            </svg>
                        </button>
                        <div x-show="sub" x-cloak class="pb-2 pl-3 space-y-0.5">
                                                                                                <a href="/so-cap" class="block py-1.5 text-sm text-muted hover:text-primary">Bán sơ cấp</a>
                                                                    <a href="/thu-cap" class="block py-1.5 text-sm text-muted hover:text-primary">Bán thứ cấp</a>
                                                                                                                                <a href="/du-an" class="block py-1.5 text-sm text-muted hover:text-primary">Tất cả dự án</a>
                                                                    <a href="/du-an?featured=1" class="block py-1.5 text-sm text-muted hover:text-primary">Dự án nổi bật</a>
                                                                                    </div>
                    </div>
                                                                <div x-data="{ sub: false }" class="border-b border-line/50">
                        <button type="button" @click="sub = !sub"
                                class="flex w-full items-center justify-between py-2.5 text-sm font-semibold text-ink">
                            Thuê
                            <svg class="w-4 h-4 text-muted transition-transform duration-150" :class="sub && 'rotate-180'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                            </svg>
                        </button>
                        <div x-show="sub" x-cloak class="pb-2 pl-3 space-y-0.5">
                                                                                                <a href="/leasing/estate-for-rent" class="block py-1.5 text-sm text-muted hover:text-primary">Nhà ở cho thuê</a>
                                                                    <a href="/commercial-leasing" class="block py-1.5 text-sm text-muted hover:text-primary">Mặt bằng thương mại</a>
                                                                                    </div>
                    </div>
                                                                <a href="/du-an" class="flex items-center py-2.5 text-sm font-semibold text-ink hover:text-primary border-b border-line/50 last:border-0">Dự án</a>
                                                                <a href="/blog" class="flex items-center py-2.5 text-sm font-semibold text-ink hover:text-primary border-b border-line/50 last:border-0">Tin tức</a>
                                                                <a href="/lien-he" class="flex items-center py-2.5 text-sm font-semibold text-ink hover:text-primary border-b border-line/50 last:border-0">Liên hệ</a>
                                        <div class="pt-4 pb-2 flex gap-2">
                                    <a href="https://vinhomesonline.vn/login" class="flex-1 text-center rounded-lg border border-line px-4 py-2.5 text-sm font-semibold text-ink">Đăng nhập</a>
                                                    <a href="https://vinhomesonline.vn/dang-ky-dai-ly" class="flex-1 text-center rounded-lg bg-accent-cta px-4 py-2.5 text-sm font-bold text-white">Đăng tin</a>
                            </div>
        </nav>
    </div>
</header>

    <main class="flex-1">
        <div class="bg-[#f8f9fb] min-h-screen">
        <section class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-6 lg:py-10"
                 x-data="listingSearch(JSON.parse('{\u0022filters\u0022:{\u0022type\u0022:\u0022rent\u0022,\u0022property_type\u0022:[],\u0022project\u0022:null,\u0022zone\u0022:null,\u0022price_min\u0022:null,\u0022price_max\u0022:null,\u0022area_min\u0022:null,\u0022area_max\u0022:null,\u0022bedrooms\u0022:[],\u0022direction\u0022:[],\u0022finishing_status\u0022:null,\u0022q\u0022:null,\u0022sort\u0022:\u0022relevance\u0022,\u0022page\u0022:1,\u0022view\u0022:\u0022grid\u0022,\u0022lat_min\u0022:null,\u0022lat_max\u0022:null,\u0022lng_min\u0022:null,\u0022lng_max\u0022:null},\u0022data\u0022:[{\u0022unit_id\u0022:420,\u0022slug\u0022:\u0022p5-c024-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Biệt thự song lập C024 — Khu đô thị Thiên Phú Park\u0022,\u0022unit_code\u0022:\u0022C024\u0022,\u0022availability\u0022:\u0022sold\u0022,\u0022availability_label\u0022:\u0022Đã bán\u0022,\u0022property_type\u0022:\u0022villa_duplex\u0022,\u0022property_type_label\u0022:\u0022Biệt thự song lập\u0022,\u0022bedrooms\u0022:3,\u0022toilets\u0022:3,\u0022area_net\u0022:242,\u0022price_from\u0022:null,\u0022rent_from\u0022:26526549,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-07.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Thiên Phú Park\u0022,\u0022slug\u0022:\u0022khu-do-thi-thien-phu-park\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Phong Lan\u0022,\u0022slug\u0022:\u0022phan-khu-phong-lan\u0022},\u0022location\u0022:\u0022Văn Giang, Hưng Yên\u0022,\u0022lat\u0022:20.9316,\u0022lng\u0022:105.9612},{\u0022unit_id\u0022:360,\u0022slug\u0022:\u0022p5-a010-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Penthouse A010 — Khu đô thị Thiên Phú Park\u0022,\u0022unit_code\u0022:\u0022A010\u0022,\u0022availability\u0022:\u0022sold\u0022,\u0022availability_label\u0022:\u0022Đã bán\u0022,\u0022property_type\u0022:\u0022penthouse\u0022,\u0022property_type_label\u0022:\u0022Penthouse\u0022,\u0022bedrooms\u0022:4,\u0022toilets\u0022:3,\u0022area_net\u0022:260,\u0022price_from\u0022:null,\u0022rent_from\u0022:62208250,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-12.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Thiên Phú Park\u0022,\u0022slug\u0022:\u0022khu-do-thi-thien-phu-park\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Hương Sen\u0022,\u0022slug\u0022:\u0022phan-khu-huong-sen\u0022},\u0022location\u0022:\u0022Văn Giang, Hưng Yên\u0022,\u0022lat\u0022:20.93,\u0022lng\u0022:105.9612},{\u0022unit_id\u0022:300,\u0022slug\u0022:\u0022p4-b008-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Nhà phố B008 — Thành phố Bình Minh Ocean\u0022,\u0022unit_code\u0022:\u0022B008\u0022,\u0022availability\u0022:\u0022sold\u0022,\u0022availability_label\u0022:\u0022Đã bán\u0022,\u0022property_type\u0022:\u0022townhouse\u0022,\u0022property_type_label\u0022:\u0022Nhà phố\u0022,\u0022bedrooms\u0022:2,\u0022toilets\u0022:4,\u0022area_net\u0022:120,\u0022price_from\u0022:null,\u0022rent_from\u0022:78397524,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-13.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Thành phố Bình Minh Ocean\u0022,\u0022slug\u0022:\u0022thanh-pho-binh-minh-ocean\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Nắng Vàng\u0022,\u0022slug\u0022:\u0022phan-khu-nang-vang\u0022},\u0022location\u0022:\u0022Cam Lâm, Khánh Hòa\u0022,\u0022lat\u0022:12.0732,\u0022lng\u0022:109.1504},{\u0022unit_id\u0022:240,\u0022slug\u0022:\u0022p3-b026-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Nhà phố B026 — Vịnh Ngọc Riverside\u0022,\u0022unit_code\u0022:\u0022B026\u0022,\u0022availability\u0022:\u0022sold\u0022,\u0022availability_label\u0022:\u0022Đã bán\u0022,\u0022property_type\u0022:\u0022townhouse\u0022,\u0022property_type_label\u0022:\u0022Nhà phố\u0022,\u0022bedrooms\u0022:3,\u0022toilets\u0022:2,\u0022area_net\u0022:268,\u0022price_from\u0022:null,\u0022rent_from\u0022:75516817,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-11.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Vịnh Ngọc Riverside\u0022,\u0022slug\u0022:\u0022vinh-ngoc-riverside\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Ngọc Trai\u0022,\u0022slug\u0022:\u0022phan-khu-ngoc-trai\u0022},\u0022location\u0022:\u0022Dương Kinh, Hải Phòng\u0022,\u0022lat\u0022:20.8024,\u0022lng\u0022:106.702},{\u0022unit_id\u0022:180,\u0022slug\u0022:\u0022p2-d024-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Nhà phố D024 — Đại đô thị An Lạc Garden\u0022,\u0022unit_code\u0022:\u0022D024\u0022,\u0022availability\u0022:\u0022sold\u0022,\u0022availability_label\u0022:\u0022Đã bán\u0022,\u0022property_type\u0022:\u0022townhouse\u0022,\u0022property_type_label\u0022:\u0022Nhà phố\u0022,\u0022bedrooms\u0022:4,\u0022toilets\u0022:3,\u0022area_net\u0022:76,\u0022price_from\u0022:null,\u0022rent_from\u0022:87304601,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-11.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Đại đô thị An Lạc Garden\u0022,\u0022slug\u0022:\u0022dai-do-thi-an-lac-garden\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Ruby\u0022,\u0022slug\u0022:\u0022phan-khu-ruby\u0022},\u0022location\u0022:\u0022TP. Thủ Đức, TP. Hồ Chí Minh\u0022,\u0022lat\u0022:10.8247,\u0022lng\u0022:106.7902},{\u0022unit_id\u0022:120,\u0022slug\u0022:\u0022p2-b022-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Biệt thự song lập B022 — Đại đô thị An Lạc Garden\u0022,\u0022unit_code\u0022:\u0022B022\u0022,\u0022availability\u0022:\u0022sold\u0022,\u0022availability_label\u0022:\u0022Đã bán\u0022,\u0022property_type\u0022:\u0022villa_duplex\u0022,\u0022property_type_label\u0022:\u0022Biệt thự song lập\u0022,\u0022bedrooms\u0022:3,\u0022toilets\u0022:3,\u0022area_net\u0022:299,\u0022price_from\u0022:null,\u0022rent_from\u0022:67982290,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-07.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Đại đô thị An Lạc Garden\u0022,\u0022slug\u0022:\u0022dai-do-thi-an-lac-garden\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu The Rainbow\u0022,\u0022slug\u0022:\u0022phan-khu-the-rainbow\u0022},\u0022location\u0022:\u0022TP. Thủ Đức, TP. Hồ Chí Minh\u0022,\u0022lat\u0022:10.8239,\u0022lng\u0022:106.7894},{\u0022unit_id\u0022:60,\u0022slug\u0022:\u0022p1-c014-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Văn phòng C014 — Khu đô thị Hồng Hạc City\u0022,\u0022unit_code\u0022:\u0022C014\u0022,\u0022availability\u0022:\u0022sold\u0022,\u0022availability_label\u0022:\u0022Đã bán\u0022,\u0022property_type\u0022:\u0022office\u0022,\u0022property_type_label\u0022:\u0022Văn phòng\u0022,\u0022bedrooms\u0022:3,\u0022toilets\u0022:1,\u0022area_net\u0022:320,\u0022price_from\u0022:null,\u0022rent_from\u0022:33379605,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-10.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Hồng Hạc City\u0022,\u0022slug\u0022:\u0022khu-do-thi-hong-hac-city\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Sapphire\u0022,\u0022slug\u0022:\u0022phan-khu-sapphire\u0022},\u0022location\u0022:\u0022Gia Lâm, Hà Nội\u0022,\u0022lat\u0022:21.0261,\u0022lng\u0022:105.965},{\u0022unit_id\u0022:424,\u0022slug\u0022:\u0022p5-c028-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Biệt thự song lập C028 — Khu đô thị Thiên Phú Park\u0022,\u0022unit_code\u0022:\u0022C028\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022villa_duplex\u0022,\u0022property_type_label\u0022:\u0022Biệt thự song lập\u0022,\u0022bedrooms\u0022:4,\u0022toilets\u0022:3,\u0022area_net\u0022:297,\u0022price_from\u0022:null,\u0022rent_from\u0022:55500786,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-09.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Thiên Phú Park\u0022,\u0022slug\u0022:\u0022khu-do-thi-thien-phu-park\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Phong Lan\u0022,\u0022slug\u0022:\u0022phan-khu-phong-lan\u0022},\u0022location\u0022:\u0022Văn Giang, Hưng Yên\u0022,\u0022lat\u0022:20.9332,\u0022lng\u0022:105.96},{\u0022unit_id\u0022:364,\u0022slug\u0022:\u0022p5-a014-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Nhà phố A014 — Khu đô thị Thiên Phú Park\u0022,\u0022unit_code\u0022:\u0022A014\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022townhouse\u0022,\u0022property_type_label\u0022:\u0022Nhà phố\u0022,\u0022bedrooms\u0022:5,\u0022toilets\u0022:2,\u0022area_net\u0022:179,\u0022price_from\u0022:null,\u0022rent_from\u0022:9473306,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-10.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Thiên Phú Park\u0022,\u0022slug\u0022:\u0022khu-do-thi-thien-phu-park\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Hương Sen\u0022,\u0022slug\u0022:\u0022phan-khu-huong-sen\u0022},\u0022location\u0022:\u0022Văn Giang, Hưng Yên\u0022,\u0022lat\u0022:20.9316,\u0022lng\u0022:105.96},{\u0022unit_id\u0022:304,\u0022slug\u0022:\u0022p4-b012-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Căn hộ B012 — Thành phố Bình Minh Ocean\u0022,\u0022unit_code\u0022:\u0022B012\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022apartment\u0022,\u0022property_type_label\u0022:\u0022Căn hộ\u0022,\u0022bedrooms\u0022:5,\u0022toilets\u0022:3,\u0022area_net\u0022:221,\u0022price_from\u0022:null,\u0022rent_from\u0022:40456013,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-10.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Thành phố Bình Minh Ocean\u0022,\u0022slug\u0022:\u0022thanh-pho-binh-minh-ocean\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Nắng Vàng\u0022,\u0022slug\u0022:\u0022phan-khu-nang-vang\u0022},\u0022location\u0022:\u0022Cam Lâm, Khánh Hòa\u0022,\u0022lat\u0022:12.0708,\u0022lng\u0022:109.152},{\u0022unit_id\u0022:244,\u0022slug\u0022:\u0022p3-c004-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Penthouse C004 — Vịnh Ngọc Riverside\u0022,\u0022unit_code\u0022:\u0022C004\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022penthouse\u0022,\u0022property_type_label\u0022:\u0022Penthouse\u0022,\u0022bedrooms\u0022:1,\u0022toilets\u0022:2,\u0022area_net\u0022:67,\u0022price_from\u0022:null,\u0022rent_from\u0022:64513742,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-07.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Vịnh Ngọc Riverside\u0022,\u0022slug\u0022:\u0022vinh-ngoc-riverside\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu San Hô\u0022,\u0022slug\u0022:\u0022phan-khu-san-ho\u0022},\u0022location\u0022:\u0022Dương Kinh, Hải Phòng\u0022,\u0022lat\u0022:20.8016,\u0022lng\u0022:106.7016},{\u0022unit_id\u0022:184,\u0022slug\u0022:\u0022p2-d028-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Biệt thự đơn lập D028 — Đại đô thị An Lạc Garden\u0022,\u0022unit_code\u0022:\u0022D028\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022villa_single\u0022,\u0022property_type_label\u0022:\u0022Biệt thự đơn lập\u0022,\u0022bedrooms\u0022:1,\u0022toilets\u0022:3,\u0022area_net\u0022:55,\u0022price_from\u0022:null,\u0022rent_from\u0022:51613630,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-07.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Đại đô thị An Lạc Garden\u0022,\u0022slug\u0022:\u0022dai-do-thi-an-lac-garden\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Ruby\u0022,\u0022slug\u0022:\u0022phan-khu-ruby\u0022},\u0022location\u0022:\u0022TP. Thủ Đức, TP. Hồ Chí Minh\u0022,\u0022lat\u0022:10.8263,\u0022lng\u0022:106.789},{\u0022unit_id\u0022:124,\u0022slug\u0022:\u0022p2-b026-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Biệt thự đơn lập B026 — Đại đô thị An Lạc Garden\u0022,\u0022unit_code\u0022:\u0022B026\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022villa_single\u0022,\u0022property_type_label\u0022:\u0022Biệt thự đơn lập\u0022,\u0022bedrooms\u0022:3,\u0022toilets\u0022:1,\u0022area_net\u0022:136,\u0022price_from\u0022:null,\u0022rent_from\u0022:19837709,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-11.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Đại đô thị An Lạc Garden\u0022,\u0022slug\u0022:\u0022dai-do-thi-an-lac-garden\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu The Rainbow\u0022,\u0022slug\u0022:\u0022phan-khu-the-rainbow\u0022},\u0022location\u0022:\u0022TP. Thủ Đức, TP. Hồ Chí Minh\u0022,\u0022lat\u0022:10.8255,\u0022lng\u0022:106.791},{\u0022unit_id\u0022:64,\u0022slug\u0022:\u0022p1-c018-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Biệt thự tứ lập C018 — Khu đô thị Hồng Hạc City\u0022,\u0022unit_code\u0022:\u0022C018\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022villa_quad\u0022,\u0022property_type_label\u0022:\u0022Biệt thự tứ lập\u0022,\u0022bedrooms\u0022:2,\u0022toilets\u0022:4,\u0022area_net\u0022:304,\u0022price_from\u0022:null,\u0022rent_from\u0022:27456673,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-09.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Hồng Hạc City\u0022,\u0022slug\u0022:\u0022khu-do-thi-hong-hac-city\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Sapphire\u0022,\u0022slug\u0022:\u0022phan-khu-sapphire\u0022},\u0022location\u0022:\u0022Gia Lâm, Hà Nội\u0022,\u0022lat\u0022:21.0277,\u0022lng\u0022:105.9666},{\u0022unit_id\u0022:4,\u0022slug\u0022:\u0022p1-a004-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Shophouse A004 — Khu đô thị Hồng Hạc City\u0022,\u0022unit_code\u0022:\u0022A004\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022shophouse\u0022,\u0022property_type_label\u0022:\u0022Shophouse\u0022,\u0022bedrooms\u0022:5,\u0022toilets\u0022:1,\u0022area_net\u0022:137,\u0022price_from\u0022:null,\u0022rent_from\u0022:40448282,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-09.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Hồng Hạc City\u0022,\u0022slug\u0022:\u0022khu-do-thi-hong-hac-city\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu The Manhattan\u0022,\u0022slug\u0022:\u0022phan-khu-the-manhattan\u0022},\u0022location\u0022:\u0022Gia Lâm, Hà Nội\u0022,\u0022lat\u0022:21.0261,\u0022lng\u0022:105.9666},{\u0022unit_id\u0022:428,\u0022slug\u0022:\u0022p5-c032-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Shophouse C032 — Khu đô thị Thiên Phú Park\u0022,\u0022unit_code\u0022:\u0022C032\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022shophouse\u0022,\u0022property_type_label\u0022:\u0022Shophouse\u0022,\u0022bedrooms\u0022:3,\u0022toilets\u0022:3,\u0022area_net\u0022:266,\u0022price_from\u0022:null,\u0022rent_from\u0022:24675456,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-13.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Thiên Phú Park\u0022,\u0022slug\u0022:\u0022khu-do-thi-thien-phu-park\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Phong Lan\u0022,\u0022slug\u0022:\u0022phan-khu-phong-lan\u0022},\u0022location\u0022:\u0022Văn Giang, Hưng Yên\u0022,\u0022lat\u0022:20.9308,\u0022lng\u0022:105.9616},{\u0022unit_id\u0022:368,\u0022slug\u0022:\u0022p5-a018-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Biệt thự shop A018 — Khu đô thị Thiên Phú Park\u0022,\u0022unit_code\u0022:\u0022A018\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022villa_shop\u0022,\u0022property_type_label\u0022:\u0022Biệt thự shop\u0022,\u0022bedrooms\u0022:3,\u0022toilets\u0022:4,\u0022area_net\u0022:223,\u0022price_from\u0022:null,\u0022rent_from\u0022:74555601,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-10.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Thiên Phú Park\u0022,\u0022slug\u0022:\u0022khu-do-thi-thien-phu-park\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Hương Sen\u0022,\u0022slug\u0022:\u0022phan-khu-huong-sen\u0022},\u0022location\u0022:\u0022Văn Giang, Hưng Yên\u0022,\u0022lat\u0022:20.9332,\u0022lng\u0022:105.9616},{\u0022unit_id\u0022:308,\u0022slug\u0022:\u0022p4-b016-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Penthouse B016 — Thành phố Bình Minh Ocean\u0022,\u0022unit_code\u0022:\u0022B016\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022penthouse\u0022,\u0022property_type_label\u0022:\u0022Penthouse\u0022,\u0022bedrooms\u0022:5,\u0022toilets\u0022:3,\u0022area_net\u0022:128,\u0022price_from\u0022:null,\u0022rent_from\u0022:87769030,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-10.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Thành phố Bình Minh Ocean\u0022,\u0022slug\u0022:\u0022thanh-pho-binh-minh-ocean\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Nắng Vàng\u0022,\u0022slug\u0022:\u0022phan-khu-nang-vang\u0022},\u0022location\u0022:\u0022Cam Lâm, Khánh Hòa\u0022,\u0022lat\u0022:12.0724,\u0022lng\u0022:109.1508},{\u0022unit_id\u0022:248,\u0022slug\u0022:\u0022p3-c008-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Studio C008 — Vịnh Ngọc Riverside\u0022,\u0022unit_code\u0022:\u0022C008\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022studio\u0022,\u0022property_type_label\u0022:\u0022Studio\u0022,\u0022bedrooms\u0022:5,\u0022toilets\u0022:3,\u0022area_net\u0022:216,\u0022price_from\u0022:null,\u0022rent_from\u0022:60761400,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-11.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Vịnh Ngọc Riverside\u0022,\u0022slug\u0022:\u0022vinh-ngoc-riverside\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu San Hô\u0022,\u0022slug\u0022:\u0022phan-khu-san-ho\u0022},\u0022location\u0022:\u0022Dương Kinh, Hải Phòng\u0022,\u0022lat\u0022:20.8032,\u0022lng\u0022:106.7004},{\u0022unit_id\u0022:188,\u0022slug\u0022:\u0022p2-d032-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Biệt thự đơn lập D032 — Đại đô thị An Lạc Garden\u0022,\u0022unit_code\u0022:\u0022D032\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022villa_single\u0022,\u0022property_type_label\u0022:\u0022Biệt thự đơn lập\u0022,\u0022bedrooms\u0022:1,\u0022toilets\u0022:2,\u0022area_net\u0022:276,\u0022price_from\u0022:null,\u0022rent_from\u0022:66457106,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-11.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Đại đô thị An Lạc Garden\u0022,\u0022slug\u0022:\u0022dai-do-thi-an-lac-garden\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Ruby\u0022,\u0022slug\u0022:\u0022phan-khu-ruby\u0022},\u0022location\u0022:\u0022TP. Thủ Đức, TP. Hồ Chí Minh\u0022,\u0022lat\u0022:10.8239,\u0022lng\u0022:106.7906},{\u0022unit_id\u0022:128,\u0022slug\u0022:\u0022p2-c004-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Studio C004 — Đại đô thị An Lạc Garden\u0022,\u0022unit_code\u0022:\u0022C004\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022studio\u0022,\u0022property_type_label\u0022:\u0022Studio\u0022,\u0022bedrooms\u0022:2,\u0022toilets\u0022:4,\u0022area_net\u0022:98,\u0022price_from\u0022:null,\u0022rent_from\u0022:38955038,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-10.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Đại đô thị An Lạc Garden\u0022,\u0022slug\u0022:\u0022dai-do-thi-an-lac-garden\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Grand Park\u0022,\u0022slug\u0022:\u0022phan-khu-grand-park\u0022},\u0022location\u0022:\u0022TP. Thủ Đức, TP. Hồ Chí Minh\u0022,\u0022lat\u0022:10.8247,\u0022lng\u0022:106.7906},{\u0022unit_id\u0022:68,\u0022slug\u0022:\u0022p1-c022-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Biệt thự shop C022 — Khu đô thị Hồng Hạc City\u0022,\u0022unit_code\u0022:\u0022C022\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022villa_shop\u0022,\u0022property_type_label\u0022:\u0022Biệt thự shop\u0022,\u0022bedrooms\u0022:4,\u0022toilets\u0022:4,\u0022area_net\u0022:250,\u0022price_from\u0022:null,\u0022rent_from\u0022:10890050,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-10.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Hồng Hạc City\u0022,\u0022slug\u0022:\u0022khu-do-thi-hong-hac-city\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Sapphire\u0022,\u0022slug\u0022:\u0022phan-khu-sapphire\u0022},\u0022location\u0022:\u0022Gia Lâm, Hà Nội\u0022,\u0022lat\u0022:21.0253,\u0022lng\u0022:105.9654},{\u0022unit_id\u0022:8,\u0022slug\u0022:\u0022p1-a008-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Nhà phố A008 — Khu đô thị Hồng Hạc City\u0022,\u0022unit_code\u0022:\u0022A008\u0022,\u0022availability\u0022:\u0022available\u0022,\u0022availability_label\u0022:\u0022Còn hàng\u0022,\u0022property_type\u0022:\u0022townhouse\u0022,\u0022property_type_label\u0022:\u0022Nhà phố\u0022,\u0022bedrooms\u0022:1,\u0022toilets\u0022:2,\u0022area_net\u0022:119,\u0022price_from\u0022:null,\u0022rent_from\u0022:32842017,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-12.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Hồng Hạc City\u0022,\u0022slug\u0022:\u0022khu-do-thi-hong-hac-city\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu The Manhattan\u0022,\u0022slug\u0022:\u0022phan-khu-the-manhattan\u0022},\u0022location\u0022:\u0022Gia Lâm, Hà Nội\u0022,\u0022lat\u0022:21.0277,\u0022lng\u0022:105.9654},{\u0022unit_id\u0022:372,\u0022slug\u0022:\u0022p5-b002-rent-a5\u0022,\u0022title\u0022:\u0022Cho thuê Nhà phố B002 — Khu đô thị Thiên Phú Park\u0022,\u0022unit_code\u0022:\u0022B002\u0022,\u0022availability\u0022:\u0022sold\u0022,\u0022availability_label\u0022:\u0022Đã bán\u0022,\u0022property_type\u0022:\u0022townhouse\u0022,\u0022property_type_label\u0022:\u0022Nhà phố\u0022,\u0022bedrooms\u0022:5,\u0022toilets\u0022:4,\u0022area_net\u0022:58,\u0022price_from\u0022:null,\u0022rent_from\u0022:60657702,\u0022price_per_m2_from\u0022:null,\u0022offers_count\u0022:1,\u0022image\u0022:\u0022\\\/images\\\/vinhomes\\\/vh-13.jpg\u0022,\u0022project\u0022:{\u0022name\u0022:\u0022Khu đô thị Thiên Phú Park\u0022,\u0022slug\u0022:\u0022khu-do-thi-thien-phu-park\u0022},\u0022zone\u0022:{\u0022name\u0022:\u0022Phân khu Hoa Mai\u0022,\u0022slug\u0022:\u0022phan-khu-hoa-mai\u0022},\u0022location\u0022:\u0022Văn Giang, Hưng Yên\u0022,\u0022lat\u0022:20.9308,\u0022lng\u0022:105.9608}],\u0022markers\u0022:[{\u0022id\u0022:420,\u0022lat\u0022:20.9316,\u0022lng\u0022:105.9612,\u0022price_from\u0022:null,\u0022rent_from\u0022:26526549,\u0022slug\u0022:\u0022p5-c024-rent-a5\u0022},{\u0022id\u0022:360,\u0022lat\u0022:20.93,\u0022lng\u0022:105.9612,\u0022price_from\u0022:null,\u0022rent_from\u0022:62208250,\u0022slug\u0022:\u0022p5-a010-rent-a5\u0022},{\u0022id\u0022:300,\u0022lat\u0022:12.0732,\u0022lng\u0022:109.1504,\u0022price_from\u0022:null,\u0022rent_from\u0022:78397524,\u0022slug\u0022:\u0022p4-b008-rent-a5\u0022},{\u0022id\u0022:240,\u0022lat\u0022:20.8024,\u0022lng\u0022:106.702,\u0022price_from\u0022:null,\u0022rent_from\u0022:75516817,\u0022slug\u0022:\u0022p3-b026-rent-a5\u0022},{\u0022id\u0022:180,\u0022lat\u0022:10.8247,\u0022lng\u0022:106.7902,\u0022price_from\u0022:null,\u0022rent_from\u0022:87304601,\u0022slug\u0022:\u0022p2-d024-rent-a5\u0022},{\u0022id\u0022:120,\u0022lat\u0022:10.8239,\u0022lng\u0022:106.7894,\u0022price_from\u0022:null,\u0022rent_from\u0022:67982290,\u0022slug\u0022:\u0022p2-b022-rent-a5\u0022},{\u0022id\u0022:60,\u0022lat\u0022:21.0261,\u0022lng\u0022:105.965,\u0022price_from\u0022:null,\u0022rent_from\u0022:33379605,\u0022slug\u0022:\u0022p1-c014-rent-a5\u0022},{\u0022id\u0022:424,\u0022lat\u0022:20.9332,\u0022lng\u0022:105.96,\u0022price_from\u0022:null,\u0022rent_from\u0022:55500786,\u0022slug\u0022:\u0022p5-c028-rent-a5\u0022},{\u0022id\u0022:364,\u0022lat\u0022:20.9316,\u0022lng\u0022:105.96,\u0022price_from\u0022:null,\u0022rent_from\u0022:9473306,\u0022slug\u0022:\u0022p5-a014-rent-a5\u0022},{\u0022id\u0022:304,\u0022lat\u0022:12.0708,\u0022lng\u0022:109.152,\u0022price_from\u0022:null,\u0022rent_from\u0022:40456013,\u0022slug\u0022:\u0022p4-b012-rent-a5\u0022},{\u0022id\u0022:244,\u0022lat\u0022:20.8016,\u0022lng\u0022:106.7016,\u0022price_from\u0022:null,\u0022rent_from\u0022:64513742,\u0022slug\u0022:\u0022p3-c004-rent-a5\u0022},{\u0022id\u0022:184,\u0022lat\u0022:10.8263,\u0022lng\u0022:106.789,\u0022price_from\u0022:null,\u0022rent_from\u0022:51613630,\u0022slug\u0022:\u0022p2-d028-rent-a5\u0022},{\u0022id\u0022:124,\u0022lat\u0022:10.8255,\u0022lng\u0022:106.791,\u0022price_from\u0022:null,\u0022rent_from\u0022:19837709,\u0022slug\u0022:\u0022p2-b026-rent-a5\u0022},{\u0022id\u0022:64,\u0022lat\u0022:21.0277,\u0022lng\u0022:105.9666,\u0022price_from\u0022:null,\u0022rent_from\u0022:27456673,\u0022slug\u0022:\u0022p1-c018-rent-a5\u0022},{\u0022id\u0022:4,\u0022lat\u0022:21.0261,\u0022lng\u0022:105.9666,\u0022price_from\u0022:null,\u0022rent_from\u0022:40448282,\u0022slug\u0022:\u0022p1-a004-rent-a5\u0022},{\u0022id\u0022:428,\u0022lat\u0022:20.9308,\u0022lng\u0022:105.9616,\u0022price_from\u0022:null,\u0022rent_from\u0022:24675456,\u0022slug\u0022:\u0022p5-c032-rent-a5\u0022},{\u0022id\u0022:368,\u0022lat\u0022:20.9332,\u0022lng\u0022:105.9616,\u0022price_from\u0022:null,\u0022rent_from\u0022:74555601,\u0022slug\u0022:\u0022p5-a018-rent-a5\u0022},{\u0022id\u0022:308,\u0022lat\u0022:12.0724,\u0022lng\u0022:109.1508,\u0022price_from\u0022:null,\u0022rent_from\u0022:87769030,\u0022slug\u0022:\u0022p4-b016-rent-a5\u0022},{\u0022id\u0022:248,\u0022lat\u0022:20.8032,\u0022lng\u0022:106.7004,\u0022price_from\u0022:null,\u0022rent_from\u0022:60761400,\u0022slug\u0022:\u0022p3-c008-rent-a5\u0022},{\u0022id\u0022:188,\u0022lat\u0022:10.8239,\u0022lng\u0022:106.7906,\u0022price_from\u0022:null,\u0022rent_from\u0022:66457106,\u0022slug\u0022:\u0022p2-d032-rent-a5\u0022},{\u0022id\u0022:128,\u0022lat\u0022:10.8247,\u0022lng\u0022:106.7906,\u0022price_from\u0022:null,\u0022rent_from\u0022:38955038,\u0022slug\u0022:\u0022p2-c004-rent-a5\u0022},{\u0022id\u0022:68,\u0022lat\u0022:21.0253,\u0022lng\u0022:105.9654,\u0022price_from\u0022:null,\u0022rent_from\u0022:10890050,\u0022slug\u0022:\u0022p1-c022-rent-a5\u0022},{\u0022id\u0022:8,\u0022lat\u0022:21.0277,\u0022lng\u0022:105.9654,\u0022price_from\u0022:null,\u0022rent_from\u0022:32842017,\u0022slug\u0022:\u0022p1-a008-rent-a5\u0022},{\u0022id\u0022:372,\u0022lat\u0022:20.9308,\u0022lng\u0022:105.9608,\u0022price_from\u0022:null,\u0022rent_from\u0022:60657702,\u0022slug\u0022:\u0022p5-b002-rent-a5\u0022}],\u0022markersAvailable\u0022:24,\u0022meta\u0022:{\u0022count\u0022:107,\u0022page\u0022:1,\u0022last_page\u0022:5,\u0022per_page\u0022:24},\u0022endpoint\u0022:\u0022http:\\\/\\\/vinhomesonline.vn\\\/api\\\/listings\u0022,\u0022type\u0022:\u0022rent\u0022}'))"
                 data-maps-key="">

            
            <header class="mb-6">
                <h1 class="font-display text-2xl sm:text-3xl font-extrabold text-primary">Nhà ở cho thuê</h1>
                <p class="mt-1 text-sm text-muted">
                    <span x-text="meta.count">107</span> bất động sản
                    <span x-show="loading" x-cloak class="ml-2 inline-flex items-center gap-1 text-primary text-xs">
                        <svg class="animate-spin h-3.5 w-3.5" fill="none" viewBox="0 0 24 24">
                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
                        </svg>
                        đang tải…
                    </span>
                </p>
            </header>

            <div class="grid grid-cols-1 lg:grid-cols-[280px_1fr] gap-6">
                
                <div class="lg:sticky lg:top-[88px] lg:self-start">
                    <aside class="rounded-xl border border-line bg-white shadow-card overflow-hidden">
    <div class="border-b border-line px-5 py-4">
        <h2 class="text-sm font-bold text-ink">Bộ lọc tìm kiếm</h2>
    </div>

    <div class="divide-y divide-line/60">
        
        <div class="px-5 py-4">
            <label class="block text-xs font-bold uppercase tracking-wide text-muted mb-2">Từ khóa</label>
            <div class="relative">
                <svg class="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted pointer-events-none" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"/>
                </svg>
                <input type="text" x-model="filters.q" @keydown.enter="applyFilters()"
                       placeholder="Tên dự án, khu vực…"
                       class="w-full rounded-lg border border-line pl-9 pr-3 py-2.5 text-sm text-ink placeholder:text-muted focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition">
            </div>
        </div>

        
        <div class="px-5 py-4">
            <p class="text-xs font-bold uppercase tracking-wide text-muted mb-3">Loại hình</p>
            <div class="space-y-2">
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="apartment"
                               :checked="filters.property_type.includes('apartment')"
                               @change="toggleArray('property_type', 'apartment')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Căn hộ</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="studio"
                               :checked="filters.property_type.includes('studio')"
                               @change="toggleArray('property_type', 'studio')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Studio</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="shophouse"
                               :checked="filters.property_type.includes('shophouse')"
                               @change="toggleArray('property_type', 'shophouse')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Shophouse</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="townhouse"
                               :checked="filters.property_type.includes('townhouse')"
                               @change="toggleArray('property_type', 'townhouse')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Nhà phố</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="villa_single"
                               :checked="filters.property_type.includes('villa_single')"
                               @change="toggleArray('property_type', 'villa_single')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Biệt thự đơn lập</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="villa_duplex"
                               :checked="filters.property_type.includes('villa_duplex')"
                               @change="toggleArray('property_type', 'villa_duplex')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Biệt thự song lập</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="villa_quad"
                               :checked="filters.property_type.includes('villa_quad')"
                               @change="toggleArray('property_type', 'villa_quad')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Biệt thự tứ lập</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="villa_shop"
                               :checked="filters.property_type.includes('villa_shop')"
                               @change="toggleArray('property_type', 'villa_shop')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Biệt thự shop</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="penthouse"
                               :checked="filters.property_type.includes('penthouse')"
                               @change="toggleArray('property_type', 'penthouse')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Penthouse</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="office"
                               :checked="filters.property_type.includes('office')"
                               @change="toggleArray('property_type', 'office')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Văn phòng</span>
                    </label>
                                    <label class="flex items-center gap-2.5 text-sm text-ink cursor-pointer group">
                        <input type="checkbox" value="retail"
                               :checked="filters.property_type.includes('retail')"
                               @change="toggleArray('property_type', 'retail')"
                               class="h-4 w-4 rounded border-line text-primary focus:ring-primary focus:ring-offset-0">
                        <span class="group-hover:text-primary transition-colors">Mặt bằng bán lẻ</span>
                    </label>
                            </div>
        </div>

        
        <div class="px-5 py-4">
            <p class="text-xs font-bold uppercase tracking-wide text-muted mb-3" x-text="isRental ? 'Giá thuê / tháng' : 'Mức giá'"></p>
            <div class="flex items-center gap-2">
                <input type="number" min="0" x-model.number="filters.price_min" placeholder="Từ"
                       class="w-full rounded-lg border border-line px-3 py-2 text-sm focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition">
                <span class="shrink-0 text-muted text-sm">–</span>
                <input type="number" min="0" x-model.number="filters.price_max" placeholder="Đến"
                       class="w-full rounded-lg border border-line px-3 py-2 text-sm focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition">
            </div>
            <p class="mt-1.5 text-[11px] text-muted">Đơn vị: VNĐ</p>
        </div>

        
        <div class="px-5 py-4">
            <p class="text-xs font-bold uppercase tracking-wide text-muted mb-3">Diện tích (m²)</p>
            <div class="flex items-center gap-2">
                <input type="number" min="0" x-model.number="filters.area_min" placeholder="Từ"
                       class="w-full rounded-lg border border-line px-3 py-2 text-sm focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition">
                <span class="shrink-0 text-muted text-sm">–</span>
                <input type="number" min="0" x-model.number="filters.area_max" placeholder="Đến"
                       class="w-full rounded-lg border border-line px-3 py-2 text-sm focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition">
            </div>
        </div>

        
        <div class="px-5 py-4">
            <p class="text-xs font-bold uppercase tracking-wide text-muted mb-3">Số phòng ngủ</p>
            <div class="flex flex-wrap gap-2">
                                    <button type="button"
                            @click="toggleArray('bedrooms', 1)"
                            :class="filters.bedrooms.includes(1) ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-3.5 py-1.5 text-sm font-semibold transition-all duration-150">
                        1
                    </button>
                                    <button type="button"
                            @click="toggleArray('bedrooms', 2)"
                            :class="filters.bedrooms.includes(2) ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-3.5 py-1.5 text-sm font-semibold transition-all duration-150">
                        2
                    </button>
                                    <button type="button"
                            @click="toggleArray('bedrooms', 3)"
                            :class="filters.bedrooms.includes(3) ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-3.5 py-1.5 text-sm font-semibold transition-all duration-150">
                        3
                    </button>
                                    <button type="button"
                            @click="toggleArray('bedrooms', 4)"
                            :class="filters.bedrooms.includes(4) ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-3.5 py-1.5 text-sm font-semibold transition-all duration-150">
                        4
                    </button>
                                    <button type="button"
                            @click="toggleArray('bedrooms', 5)"
                            :class="filters.bedrooms.includes(5) ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-3.5 py-1.5 text-sm font-semibold transition-all duration-150">
                        5+
                    </button>
                            </div>
        </div>

        
        <div class="px-5 py-4">
            <p class="text-xs font-bold uppercase tracking-wide text-muted mb-3">Hướng</p>
            <div class="flex flex-wrap gap-2">
                                    <button type="button"
                            @click="toggleArray('direction', 'east')"
                            :class="filters.direction.includes('east') ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-2.5 py-1 text-xs font-semibold transition-all duration-150">
                        Đông
                    </button>
                                    <button type="button"
                            @click="toggleArray('direction', 'west')"
                            :class="filters.direction.includes('west') ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-2.5 py-1 text-xs font-semibold transition-all duration-150">
                        Tây
                    </button>
                                    <button type="button"
                            @click="toggleArray('direction', 'south')"
                            :class="filters.direction.includes('south') ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-2.5 py-1 text-xs font-semibold transition-all duration-150">
                        Nam
                    </button>
                                    <button type="button"
                            @click="toggleArray('direction', 'north')"
                            :class="filters.direction.includes('north') ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-2.5 py-1 text-xs font-semibold transition-all duration-150">
                        Bắc
                    </button>
                                    <button type="button"
                            @click="toggleArray('direction', 'southeast')"
                            :class="filters.direction.includes('southeast') ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-2.5 py-1 text-xs font-semibold transition-all duration-150">
                        Đông Nam
                    </button>
                                    <button type="button"
                            @click="toggleArray('direction', 'northeast')"
                            :class="filters.direction.includes('northeast') ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-2.5 py-1 text-xs font-semibold transition-all duration-150">
                        Đông Bắc
                    </button>
                                    <button type="button"
                            @click="toggleArray('direction', 'southwest')"
                            :class="filters.direction.includes('southwest') ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-2.5 py-1 text-xs font-semibold transition-all duration-150">
                        Tây Nam
                    </button>
                                    <button type="button"
                            @click="toggleArray('direction', 'northwest')"
                            :class="filters.direction.includes('northwest') ? 'bg-primary text-white border-primary shadow-sm' : 'text-muted border-line hover:border-primary/50 hover:text-ink'"
                            class="rounded-lg border px-2.5 py-1 text-xs font-semibold transition-all duration-150">
                        Tây Bắc
                    </button>
                            </div>
        </div>

        
        <div x-show="isRental" x-cloak class="px-5 py-4">
            <p class="text-xs font-bold uppercase tracking-wide text-muted mb-3">Nội thất</p>
            <select x-model="filters.finishing_status" @change="applyFilters()"
                    class="w-full rounded-lg border border-line px-3 py-2.5 text-sm text-ink focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition">
                <option value="">Tất cả</option>
                                    <option value="bare_shell">Bàn giao thô</option>
                                    <option value="basic">Hoàn thiện cơ bản</option>
                                    <option value="full">Hoàn thiện đầy đủ</option>
                                    <option value="furnished">Đầy đủ nội thất</option>
                            </select>
        </div>
    </div>

    
    <div class="px-5 py-4 bg-[#f8f9fb] border-t border-line flex gap-2">
        <button type="button" @click="applyFilters()"
                class="flex-1 rounded-lg bg-primary py-2.5 text-sm font-bold text-white hover:bg-primary-hover transition-colors duration-150 shadow-sm">
            Áp dụng
        </button>
        <button type="button" @click="resetFilters()"
                class="rounded-lg border border-line bg-white px-4 py-2.5 text-sm font-semibold text-muted hover:text-ink hover:border-ink/20 transition-all duration-150">
            Đặt lại
        </button>
    </div>
</aside>
                </div>

                
                <div>
                    
                    <div class="mb-4 flex flex-wrap items-center justify-between gap-3">
                        
                        <div class="inline-flex rounded-xl border border-line bg-white shadow-card overflow-hidden">
                                                            <button type="button" @click="setView('grid')"
                                        :class="filters.view === 'grid' ? 'bg-primary text-white' : 'text-muted hover:text-ink hover:bg-line/40'"
                                        class="flex items-center gap-1.5 px-3.5 py-2 text-sm font-semibold transition-colors duration-150">
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6A2.25 2.25 0 0 1 6 3.75h2.25A2.25 2.25 0 0 1 10.5 6v2.25a2.25 2.25 0 0 1-2.25 2.25H6a2.25 2.25 0 0 1-2.25-2.25V6ZM3.75 15.75A2.25 2.25 0 0 1 6 13.5h2.25a2.25 2.25 0 0 1 2.25 2.25V18a2.25 2.25 0 0 1-2.25 2.25H6A2.25 2.25 0 0 1 3.75 18v-2.25ZM13.5 6a2.25 2.25 0 0 1 2.25-2.25H18A2.25 2.25 0 0 1 20.25 6v2.25A2.25 2.25 0 0 1 18 10.5h-2.25a2.25 2.25 0 0 1-2.25-2.25V6ZM13.5 15.75a2.25 2.25 0 0 1 2.25-2.25H18a2.25 2.25 0 0 1 2.25 2.25V18A2.25 2.25 0 0 1 18 20.25h-2.25A2.25 2.25 0 0 1 13.5 18v-2.25Z"/>
                                    </svg>
                                    <span class="hidden sm:inline">Lưới</span>
                                </button>
                                                            <button type="button" @click="setView('table')"
                                        :class="filters.view === 'table' ? 'bg-primary text-white' : 'text-muted hover:text-ink hover:bg-line/40'"
                                        class="flex items-center gap-1.5 px-3.5 py-2 text-sm font-semibold transition-colors duration-150">
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M3.375 19.5h17.25m-17.25 0a1.125 1.125 0 0 1-1.125-1.125M3.375 19.5h7.5c.621 0 1.125-.504 1.125-1.125m-9.75 0V5.625m0 12.75v-1.5c0-.621.504-1.125 1.125-1.125m18.375 2.625V5.625m0 12.75c0 .621-.504 1.125-1.125 1.125m1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125m0 3.75h-7.5A1.125 1.125 0 0 1 12 18.375m9.75-12.75c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125m19.5 0v1.5c0 .621-.504 1.125-1.125 1.125M2.25 5.625v1.5c0 .621.504 1.125 1.125 1.125m0 0h17.25m-17.25 0h7.5c.621 0 1.125.504 1.125 1.125M3.375 8.25c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125h7.5c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125m-1.5 3.75h.008v.008H9.375v-.008Zm6 0h.008v.008h-.008v-.008Zm6 0h.008v.008h-.008v-.008Z"/>
                                    </svg>
                                    <span class="hidden sm:inline">Bảng</span>
                                </button>
                                                            <button type="button" @click="setView('map')"
                                        :class="filters.view === 'map' ? 'bg-primary text-white' : 'text-muted hover:text-ink hover:bg-line/40'"
                                        class="flex items-center gap-1.5 px-3.5 py-2 text-sm font-semibold transition-colors duration-150">
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 6.75V15m6-6v8.25m.503 3.498 4.875-2.437c.381-.19.622-.58.622-1.006V4.82c0-.836-.88-1.38-1.628-1.006l-3.869 1.934c-.317.159-.69.159-1.006 0L9.503 3.252a1.125 1.125 0 0 0-1.006 0L3.622 5.689C3.24 5.88 3 6.27 3 6.695V19.18c0 .836.88 1.38 1.628 1.006l3.869-1.934c.317-.159.69-.159 1.006 0l4.994 2.497c.317.158.69.158 1.006 0Z"/>
                                    </svg>
                                    <span class="hidden sm:inline">Bản đồ</span>
                                </button>
                                                    </div>

                        
                        <div class="flex items-center gap-2">
                            <label class="text-xs text-muted font-medium hidden sm:inline">Sắp xếp:</label>
                            <select x-model="filters.sort" @change="setSort(filters.sort)"
                                    class="rounded-xl border border-line bg-white px-3 py-2 text-sm font-medium text-ink shadow-card focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition">
                                <option value="relevance">Liên quan nhất</option>
                                <option value="newest">Mới nhất</option>
                                <option value="price_asc">Giá thấp → cao</option>
                                <option value="price_desc">Giá cao → thấp</option>
                                <option value="ppm2_asc">Giá/m² thấp → cao</option>
                                <option value="ppm2_desc">Giá/m² cao → thấp</option>
                                <option value="area_asc">Diện tích nhỏ → lớn</option>
                                <option value="area_desc">Diện tích lớn → nhỏ</option>
                            </select>
                        </div>
                    </div>

                    
                    <div x-show="!ready">
                                                    <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-4">
                                                                    <a href="/tin/p5-c024-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-07.jpg" alt="Cho thuê Biệt thự song lập C024 — Khu đô thị Thiên Phú Park" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-muted px-2.5 py-1 text-xs font-semibold text-white shadow-card">Đã bán</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 420, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: C024
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">27 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Biệt thự song lập C024 — Khu đô thị Thiên Phú Park
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Văn Giang, Hưng Yên</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Biệt thự song lập</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    3 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">242 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p5-a010-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-12.jpg" alt="Cho thuê Penthouse A010 — Khu đô thị Thiên Phú Park" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-muted px-2.5 py-1 text-xs font-semibold text-white shadow-card">Đã bán</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 360, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: A010
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">62 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Penthouse A010 — Khu đô thị Thiên Phú Park
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Văn Giang, Hưng Yên</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Penthouse</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    4 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">260 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p4-b008-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-13.jpg" alt="Cho thuê Nhà phố B008 — Thành phố Bình Minh Ocean" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-muted px-2.5 py-1 text-xs font-semibold text-white shadow-card">Đã bán</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 300, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: B008
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">78 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Nhà phố B008 — Thành phố Bình Minh Ocean
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Cam Lâm, Khánh Hòa</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Nhà phố</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    2 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">4 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">120 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p3-b026-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-11.jpg" alt="Cho thuê Nhà phố B026 — Vịnh Ngọc Riverside" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-muted px-2.5 py-1 text-xs font-semibold text-white shadow-card">Đã bán</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 240, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: B026
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">76 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Nhà phố B026 — Vịnh Ngọc Riverside
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Dương Kinh, Hải Phòng</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Nhà phố</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    3 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">2 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">268 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p2-d024-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-11.jpg" alt="Cho thuê Nhà phố D024 — Đại đô thị An Lạc Garden" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-muted px-2.5 py-1 text-xs font-semibold text-white shadow-card">Đã bán</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 180, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: D024
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">87 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Nhà phố D024 — Đại đô thị An Lạc Garden
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">TP. Thủ Đức, TP. Hồ Chí Minh</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Nhà phố</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    4 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">76 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p2-b022-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-07.jpg" alt="Cho thuê Biệt thự song lập B022 — Đại đô thị An Lạc Garden" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-muted px-2.5 py-1 text-xs font-semibold text-white shadow-card">Đã bán</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 120, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: B022
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">68 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Biệt thự song lập B022 — Đại đô thị An Lạc Garden
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">TP. Thủ Đức, TP. Hồ Chí Minh</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Biệt thự song lập</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    3 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">299 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p1-c014-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-10.jpg" alt="Cho thuê Văn phòng C014 — Khu đô thị Hồng Hạc City" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-muted px-2.5 py-1 text-xs font-semibold text-white shadow-card">Đã bán</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 60, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: C014
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">33 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Văn phòng C014 — Khu đô thị Hồng Hạc City
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Gia Lâm, Hà Nội</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Văn phòng</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    3 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">1 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">320 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p5-c028-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-09.jpg" alt="Cho thuê Biệt thự song lập C028 — Khu đô thị Thiên Phú Park" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 424, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: C028
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">56 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Biệt thự song lập C028 — Khu đô thị Thiên Phú Park
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Văn Giang, Hưng Yên</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Biệt thự song lập</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    4 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">297 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p5-a014-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-10.jpg" alt="Cho thuê Nhà phố A014 — Khu đô thị Thiên Phú Park" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 364, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: A014
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">9 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Nhà phố A014 — Khu đô thị Thiên Phú Park
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Văn Giang, Hưng Yên</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Nhà phố</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    5 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">2 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">179 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p4-b012-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-10.jpg" alt="Cho thuê Căn hộ B012 — Thành phố Bình Minh Ocean" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 304, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: B012
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">40 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Căn hộ B012 — Thành phố Bình Minh Ocean
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Cam Lâm, Khánh Hòa</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Căn hộ</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    5 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">221 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p3-c004-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-07.jpg" alt="Cho thuê Penthouse C004 — Vịnh Ngọc Riverside" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 244, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: C004
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">65 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Penthouse C004 — Vịnh Ngọc Riverside
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Dương Kinh, Hải Phòng</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Penthouse</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    1 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">2 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">67 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p2-d028-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-07.jpg" alt="Cho thuê Biệt thự đơn lập D028 — Đại đô thị An Lạc Garden" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 184, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: D028
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">52 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Biệt thự đơn lập D028 — Đại đô thị An Lạc Garden
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">TP. Thủ Đức, TP. Hồ Chí Minh</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Biệt thự đơn lập</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    1 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">55 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p2-b026-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-11.jpg" alt="Cho thuê Biệt thự đơn lập B026 — Đại đô thị An Lạc Garden" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 124, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: B026
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">20 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Biệt thự đơn lập B026 — Đại đô thị An Lạc Garden
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">TP. Thủ Đức, TP. Hồ Chí Minh</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Biệt thự đơn lập</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    3 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">1 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">136 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p1-c018-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-09.jpg" alt="Cho thuê Biệt thự tứ lập C018 — Khu đô thị Hồng Hạc City" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 64, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: C018
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">27 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Biệt thự tứ lập C018 — Khu đô thị Hồng Hạc City
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Gia Lâm, Hà Nội</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Biệt thự tứ lập</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    2 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">4 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">304 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p1-a004-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-09.jpg" alt="Cho thuê Shophouse A004 — Khu đô thị Hồng Hạc City" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 4, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: A004
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">40 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Shophouse A004 — Khu đô thị Hồng Hạc City
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Gia Lâm, Hà Nội</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Shophouse</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    5 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">1 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">137 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p5-c032-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-13.jpg" alt="Cho thuê Shophouse C032 — Khu đô thị Thiên Phú Park" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 428, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: C032
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">25 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Shophouse C032 — Khu đô thị Thiên Phú Park
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Văn Giang, Hưng Yên</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Shophouse</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    3 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">266 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p5-a018-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-10.jpg" alt="Cho thuê Biệt thự shop A018 — Khu đô thị Thiên Phú Park" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 368, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: A018
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">75 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Biệt thự shop A018 — Khu đô thị Thiên Phú Park
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Văn Giang, Hưng Yên</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Biệt thự shop</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    3 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">4 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">223 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p4-b016-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-10.jpg" alt="Cho thuê Penthouse B016 — Thành phố Bình Minh Ocean" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 308, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: B016
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">88 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Penthouse B016 — Thành phố Bình Minh Ocean
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Cam Lâm, Khánh Hòa</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Penthouse</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    5 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">128 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p3-c008-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-11.jpg" alt="Cho thuê Studio C008 — Vịnh Ngọc Riverside" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 248, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: C008
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">61 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Studio C008 — Vịnh Ngọc Riverside
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Dương Kinh, Hải Phòng</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Studio</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    5 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">3 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">216 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p2-d032-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-11.jpg" alt="Cho thuê Biệt thự đơn lập D032 — Đại đô thị An Lạc Garden" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 188, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: D032
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">66 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Biệt thự đơn lập D032 — Đại đô thị An Lạc Garden
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">TP. Thủ Đức, TP. Hồ Chí Minh</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Biệt thự đơn lập</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    1 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">2 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">276 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p2-c004-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-10.jpg" alt="Cho thuê Studio C004 — Đại đô thị An Lạc Garden" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 128, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: C004
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">39 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Studio C004 — Đại đô thị An Lạc Garden
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">TP. Thủ Đức, TP. Hồ Chí Minh</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Studio</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    2 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">4 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">98 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p1-c022-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-10.jpg" alt="Cho thuê Biệt thự shop C022 — Khu đô thị Hồng Hạc City" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 68, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: C022
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">11 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Biệt thự shop C022 — Khu đô thị Hồng Hạc City
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Gia Lâm, Hà Nội</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Biệt thự shop</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    4 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">4 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">250 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p1-a008-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-12.jpg" alt="Cho thuê Nhà phố A008 — Khu đô thị Hồng Hạc City" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-success px-2.5 py-1 text-xs font-semibold text-white shadow-card">Còn hàng</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 8, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: A008
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">33 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Nhà phố A008 — Khu đô thị Hồng Hạc City
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Gia Lâm, Hà Nội</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Nhà phố</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    1 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">2 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">119 m²</span>
                    </div>
    </div>
</a>
                                                                    <a href="/tin/p5-b002-rent-a5"
   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">

    
    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
        <div class="relative aspect-[4/3] overflow-hidden bg-line">
                    <img src="/images/vinhomes/vh-13.jpg" alt="Cho thuê Nhà phố B002 — Khu đô thị Thiên Phú Park" loading="lazy"
                          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
    
    <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                <span class="rounded-md bg-muted px-2.5 py-1 text-xs font-semibold text-white shadow-card">Đã bán</span>
                            </div>

            
                            <button type="button"
        x-data="favoriteToggle({ unitId: 372, favorited: false })"
        @click.prevent.stop="toggle()"
        :aria-pressed="favorited.toString()"
        aria-label="Lưu tin"
        class="absolute right-3 top-3 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
    <svg class="h-5 w-5" :class="favorited ? 'text-error' : 'text-muted'"
         :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
    </svg>
</button>
            
            
                            <span class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm">
                    Mã: B002
                </span>
</div>
    </div>

    
    <div class="flex flex-1 flex-col p-4">
        
        <div class="flex items-baseline justify-between gap-2 mb-2">
            <span class="font-display text-xl font-extrabold text-accent leading-none">61 triệu/tháng</span>
                    </div>

        
        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug">
            Cho thuê Nhà phố B002 — Khu đô thị Thiên Phú Park
        </h3>

        
                    <p class="mt-1.5 flex items-center gap-1 text-xs text-muted">
                <svg class="h-3.5 w-3.5 shrink-0 text-muted/70" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/>
                </svg>
                <span class="line-clamp-1">Văn Giang, Hưng Yên</span>
            </p>
        
        
        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                            <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">Nhà phố</span>
                                        <span class="inline-flex items-center gap-1 rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">
                    <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12h19.5m-7.5-9v9m-4.5-9v9M2.25 3h19.5"/></svg>
                    5 PN
                </span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">4 WC</span>
                                        <span class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted">58 m²</span>
                    </div>
    </div>
</a>
                                                            </div>
                            <nav class="mt-8"><nav role="navigation" aria-label="Pagination Navigation">

        <div class="flex gap-2 items-center justify-between sm:hidden">

                            <span class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-600 bg-white border border-gray-300 cursor-not-allowed leading-5 rounded-md dark:text-gray-300 dark:bg-gray-700 dark:border-gray-600">
                    pagination.previous
                </span>
            
                            <a href="https://vinhomesonline.vn/leasing/estate-for-rent?page=2" rel="next" class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-800 bg-white border border-gray-300 leading-5 rounded-md hover:text-gray-700 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-800 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-200 dark:focus:border-blue-700 dark:active:bg-gray-700 dark:active:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-900 dark:hover:text-gray-200">
                    pagination.next
                </a>
            
        </div>

        <div class="hidden sm:flex-1 sm:flex sm:gap-2 sm:items-center sm:justify-between">

            <div>
                <p class="text-sm text-gray-700 leading-5 dark:text-gray-600">
                    Showing
                                            <span class="font-medium">1</span>
                        to
                        <span class="font-medium">24</span>
                                        of
                    <span class="font-medium">107</span>
                    results
                </p>
            </div>

            <div>
                <span class="inline-flex rtl:flex-row-reverse shadow-sm rounded-md">

                    
                                            <span aria-disabled="true" aria-label="pagination.previous">
                            <span class="inline-flex items-center px-2 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 cursor-not-allowed rounded-l-md leading-5 dark:bg-gray-700 dark:border-gray-600 dark:text-gray-400" aria-hidden="true">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                                    <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                                </svg>
                            </span>
                        </span>
                    
                    
                                            
                        
                        
                                                                                                                        <span aria-current="page">
                                        <span class="inline-flex items-center px-4 py-2 -ml-px text-sm font-medium text-gray-700 bg-gray-200 border border-gray-300 cursor-default leading-5 dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300">1</span>
                                    </span>
                                                                                                                                <a href="https://vinhomesonline.vn/leasing/estate-for-rent?page=2" class="inline-flex items-center px-4 py-2 -ml-px text-sm font-medium text-gray-700 bg-white border border-gray-300 leading-5 hover:text-gray-700 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-700 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-300 dark:hover:text-gray-300 dark:active:bg-gray-700 dark:focus:border-blue-800 hover:bg-gray-100 dark:hover:bg-gray-900" aria-label="Go to page 2">
                                        2
                                    </a>
                                                                                                                                <a href="https://vinhomesonline.vn/leasing/estate-for-rent?page=3" class="inline-flex items-center px-4 py-2 -ml-px text-sm font-medium text-gray-700 bg-white border border-gray-300 leading-5 hover:text-gray-700 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-700 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-300 dark:hover:text-gray-300 dark:active:bg-gray-700 dark:focus:border-blue-800 hover:bg-gray-100 dark:hover:bg-gray-900" aria-label="Go to page 3">
                                        3
                                    </a>
                                                                                                                                <a href="https://vinhomesonline.vn/leasing/estate-for-rent?page=4" class="inline-flex items-center px-4 py-2 -ml-px text-sm font-medium text-gray-700 bg-white border border-gray-300 leading-5 hover:text-gray-700 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-700 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-300 dark:hover:text-gray-300 dark:active:bg-gray-700 dark:focus:border-blue-800 hover:bg-gray-100 dark:hover:bg-gray-900" aria-label="Go to page 4">
                                        4
                                    </a>
                                                                                                                                <a href="https://vinhomesonline.vn/leasing/estate-for-rent?page=5" class="inline-flex items-center px-4 py-2 -ml-px text-sm font-medium text-gray-700 bg-white border border-gray-300 leading-5 hover:text-gray-700 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-700 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-300 dark:hover:text-gray-300 dark:active:bg-gray-700 dark:focus:border-blue-800 hover:bg-gray-100 dark:hover:bg-gray-900" aria-label="Go to page 5">
                                        5
                                    </a>
                                                                                                        
                    
                                            <a href="https://vinhomesonline.vn/leasing/estate-for-rent?page=2" rel="next" class="inline-flex items-center px-2 py-2 -ml-px text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-r-md leading-5 hover:text-gray-400 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-500 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:active:bg-gray-700 dark:focus:border-blue-800 dark:text-gray-300 dark:hover:bg-gray-900 dark:hover:text-gray-300" aria-label="pagination.next">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                            </svg>
                        </a>
                                    </span>
            </div>
        </div>
    </nav>
</nav>
                                            </div>

                    
                    <div x-show="ready" x-cloak>
                        
                        <template x-if="items.length === 0">
                            <div class="rounded-xl border border-line bg-white p-12 text-center shadow-card">
                                <svg class="mx-auto h-12 w-12 text-muted/40" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"/>
                                </svg>
                                <p class="mt-4 font-semibold text-ink">Không có kết quả phù hợp</p>
                                <p class="mt-1 text-sm text-muted">Thử thay đổi bộ lọc hoặc từ khóa tìm kiếm.</p>
                                <button type="button" @click="resetFilters()"
                                        class="mt-4 rounded-lg bg-primary px-5 py-2.5 text-sm font-bold text-white hover:bg-primary-hover transition-colors">
                                    Xóa bộ lọc
                                </button>
                            </div>
                        </template>

                        
                        <div x-show="filters.view === 'grid' && items.length"
                             class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-4">
                            <template x-for="card in items" :key="card.unit_id">
                                <a :href="'/tin/' + card.slug"
                                   class="group relative flex flex-col overflow-hidden rounded-xl border border-line bg-white shadow-card transition-all duration-200 hover:-translate-y-1 hover:shadow-raised">
                                    <div class="relative aspect-[4/3] overflow-hidden bg-line/60">
                                        <template x-if="card.image">
                                            <img :src="card.image" :alt="card.title" loading="lazy"
                                                 class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105">
                                        </template>
                                        <template x-if="!card.image">
                                            <div class="absolute inset-0 transition-transform duration-300 group-hover:scale-105" :style="placeholderStyle(card)">
                                                <svg class="absolute -bottom-6 -right-5 h-36 w-36 text-white/[0.07]" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 21V9l9-6 9 6v12h-6v-7H9v7H3z"/></svg>
                                                <span class="absolute inset-0 flex select-none items-center justify-center font-display text-5xl font-extrabold text-white/85" x-text="initial(card)"></span>
                                            </div>
                                        </template>
                                        
                                        <div class="absolute left-3 top-3 z-10 flex flex-col items-start gap-1.5">
                                            <span x-show="card.availability_label" x-cloak
                                                  class="rounded-md px-2.5 py-1 text-xs font-semibold text-white shadow-card"
                                                  :class="statusClass(card)" x-text="card.availability_label"></span>
                                            <span x-show="card.offers_count > 1" x-cloak
                                                  class="inline-flex items-center gap-1 rounded-full bg-primary/90 px-2.5 py-1 text-[11px] font-semibold text-white backdrop-blur-sm"
                                                  x-text="card.offers_count + ' môi giới'"></span>
                                        </div>
                                        
                                        <button type="button"
                                                x-data="favoriteToggle({ unitId: card.unit_id, favorited: false })"
                                                @click.prevent.stop="toggle()" aria-label="Lưu tin"
                                                class="absolute right-3 top-3 z-10 inline-flex h-8 w-8 items-center justify-center rounded-full bg-white/90 shadow-card backdrop-blur transition hover:bg-white">
                                            <svg class="h-4 w-4" :class="favorited ? 'text-error' : 'text-muted'"
                                                 :fill="favorited ? 'currentColor' : 'none'" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z"/>
                                            </svg>
                                        </button>
                                        
                                        <span x-show="card.unit_code" x-cloak
                                              class="absolute bottom-0 right-0 rounded-tl-lg bg-black/60 px-2.5 py-1 text-[11px] font-medium text-white backdrop-blur-sm"
                                              x-text="'Mã: ' + card.unit_code"></span>
                                    </div>
                                    <div class="flex flex-1 flex-col p-4">
                                        
                                        <div class="flex items-baseline justify-between gap-2 mb-2">
                                            <span class="font-display text-xl font-extrabold text-accent leading-none" x-text="money(card)"></span>
                                            <span x-show="ppm2(card)" class="text-[11px] text-muted shrink-0" x-text="ppm2(card)"></span>
                                        </div>
                                        <h3 class="line-clamp-2 text-sm font-semibold text-ink group-hover:text-primary transition-colors duration-150 leading-snug" x-text="card.title"></h3>
                                        <p class="mt-1.5 text-xs text-muted flex items-center gap-1" x-show="card.location" x-cloak>
                                            <svg class="h-3.5 w-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z"/></svg>
                                            <span class="line-clamp-1" x-text="card.location"></span>
                                        </p>
                                        <div class="mt-2.5 flex flex-wrap items-center gap-1.5">
                                            <span x-show="card.property_type_label" x-cloak class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted" x-text="card.property_type_label"></span>
                                            <span x-show="card.bedrooms" x-cloak class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted" x-text="card.bedrooms + ' PN'"></span>
                                            <span x-show="card.toilets" x-cloak class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted" x-text="card.toilets + ' WC'"></span>
                                            <span x-show="card.area_net" x-cloak class="rounded-md bg-line/70 px-2 py-0.5 text-[11px] font-medium text-muted" x-text="card.area_net + ' m²'"></span>
                                        </div>
                                    </div>
                                </a>
                            </template>
                        </div>

                        
                        <div x-show="filters.view === 'table' && items.length" x-cloak>
                            <div class="rounded-xl border border-line bg-white shadow-card overflow-hidden">
                                <table class="w-full text-sm">
                                    <thead>
                                        <tr class="border-b border-line bg-[#f8f9fb] text-left">
                                            <th class="px-4 py-3 text-xs font-bold uppercase tracking-wide text-muted">Tin đăng</th>
                                            <th class="px-4 py-3 text-xs font-bold uppercase tracking-wide text-muted hidden sm:table-cell">Loại</th>
                                            <th class="px-4 py-3 text-xs font-bold uppercase tracking-wide text-muted hidden md:table-cell">PN</th>
                                            <th class="px-4 py-3 text-xs font-bold uppercase tracking-wide text-muted hidden md:table-cell">DT</th>
                                            <th class="px-4 py-3 text-xs font-bold uppercase tracking-wide text-muted">Giá</th>
                                            <th class="px-4 py-3 text-xs font-bold uppercase tracking-wide text-muted hidden lg:table-cell">Môi giới</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-line/60">
                                        <template x-for="card in items" :key="'r' + card.unit_id">
                                            <tr class="hover:bg-[#f8f9fb] transition-colors">
                                                <td class="px-4 py-3"><a :href="'/tin/' + card.slug" class="font-semibold text-ink hover:text-primary transition-colors" x-text="card.title"></a></td>
                                                <td class="px-4 py-3 text-muted hidden sm:table-cell" x-text="card.property_type_label"></td>
                                                <td class="px-4 py-3 text-muted hidden md:table-cell" x-text="card.bedrooms"></td>
                                                <td class="px-4 py-3 text-muted hidden md:table-cell" x-text="card.area_net ? card.area_net + ' m²' : '—'"></td>
                                                <td class="px-4 py-3 font-bold text-accent" x-text="money(card)"></td>
                                                <td class="px-4 py-3 text-muted hidden lg:table-cell" x-text="card.offers_count"></td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        
                        <div x-show="filters.view === 'map'" x-cloak>
                            <p class="mb-2 text-xs text-muted"
                               x-show="markersAvailable < meta.count" x-cloak>
                                Hiển thị <span x-text="markersAvailable"></span> / <span x-text="meta.count"></span> vị trí.
                            </p>
                            <template x-if="!$root.dataset.mapsKey">
                                <div class="rounded-xl border border-line bg-white p-8 text-center text-sm text-muted shadow-card">
                                    Bản đồ cần cấu hình khóa Google Maps.
                                </div>
                            </template>
                            <div x-ref="map" class="h-[560px] w-full rounded-xl border border-line bg-line shadow-card"
                                 x-show="$root.dataset.mapsKey"></div>
                        </div>

                        
                        <nav x-show="meta.last_page > 1 && items.length" x-cloak
                             class="mt-8 flex items-center justify-center gap-1.5">
                            <button type="button" @click="goPage(meta.page - 1)" :disabled="meta.page <= 1"
                                    class="rounded-lg border border-line bg-white px-3.5 py-2 text-sm font-semibold text-muted hover:text-ink disabled:opacity-40 shadow-card transition">‹</button>
                            <template x-for="p in pageNumbers" :key="'p' + p">
                                <button type="button" @click="goPage(p)"
                                        :class="p === meta.page ? 'bg-primary text-white border-primary shadow-sm' : 'bg-white border-line text-ink hover:border-primary/40'"
                                        class="rounded-lg border px-3.5 py-2 text-sm font-semibold transition-all" x-text="p"></button>
                            </template>
                            <button type="button" @click="goPage(meta.page + 1)" :disabled="meta.page >= meta.last_page"
                                    class="rounded-lg border border-line bg-white px-3.5 py-2 text-sm font-semibold text-muted hover:text-ink disabled:opacity-40 shadow-card transition">›</button>
                        </nav>
                    </div>
                </div>
            </div>
        </section>
    </div>
    </main>

    <footer class="mt-16 bg-primary-darker text-white">
    
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 pt-12 pb-8">
        <div class="grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
            
            <div class="sm:col-span-2 lg:col-span-1">
                <div class="flex items-center gap-2 mb-3">
                    <span class="inline-flex h-8 w-8 items-center justify-center rounded-lg bg-white/15 text-white font-extrabold text-sm">V</span>
                    <span class="font-display text-lg font-extrabold uppercase tracking-tight">Vinhomes Online</span>
                </div>
                <p class="text-sm text-white/65 leading-relaxed">Sàn giao dịch bất động sản</p>

                
                <a href="tel:19001234"
                   class="mt-5 inline-flex items-center gap-2 rounded-lg bg-white/10 px-4 py-2.5 text-sm font-bold hover:bg-white/20 transition-colors">
                    <svg class="h-4 w-4 text-accent-cta" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z"/>
                    </svg>
                    1900 1234
                </a>

                
                <div class="mt-5">
                    <p class="text-xs font-bold uppercase tracking-wide text-white/60 mb-2">Đăng ký nhận tin</p>
                    <div class="[&_input]:bg-white/10 [&_input]:border-white/20 [&_input]:text-white [&_input]:placeholder:text-white/40 [&_input]:rounded-lg [&_input]:text-sm">
                        <div x-data="{
        email: '',
        website: '',
        submitting: false,
        done: false,
        error: '',
        async submit() {
            this.submitting = true; this.error = '';
            try {
                const res = await fetch('/api/newsletter/subscribe', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', Accept: 'application/json', 'X-Requested-With': 'XMLHttpRequest' },
                    body: JSON.stringify({ email: this.email, website: this.website }),
                });
                if (res.status === 201) { this.done = true; return; }
                if (res.status === 429) { this.error = 'Bạn thao tác quá nhanh, vui lòng thử lại sau.'; return; }
                const body = await res.json().catch(() => ({}));
                this.error = body?.errors?.email?.[0] || 'Đăng ký không thành công.';
            } catch (e) {
                this.error = 'Không thể kết nối. Vui lòng thử lại.';
            } finally { this.submitting = false; }
        }
     }">
        
    <div x-show="done" x-cloak class="mt-3 rounded-md bg-primary/10 px-4 py-3 text-sm text-primary">
        Cảm ơn bạn đã đăng ký nhận tin!
    </div>

    <form x-show="!done" @submit.prevent="submit()" class="mt-3 flex w-full flex-col sm:flex-row gap-2">
        <input type="email" x-model="email" required placeholder="Nhập email của bạn"
               class="min-w-0 flex-1 rounded-md border border-line px-4 py-2.5 text-sm focus:outline-none focus:border-primary">
        
        <input type="text" x-model="website" tabindex="-1" autocomplete="off" class="hidden" aria-hidden="true">
        <button type="submit" :disabled="submitting"
                class="rounded-md bg-accent-cta px-5 py-2.5 text-sm font-semibold text-white hover:opacity-90 transition-opacity duration-150 disabled:opacity-60 whitespace-nowrap">
            <span x-show="!submitting">Đăng ký</span>
            <span x-show="submitting" x-cloak>…</span>
        </button>
    </form>
    <p x-show="error" x-text="error" x-cloak class="mt-1 text-xs text-red-600"></p>
</div>
                    </div>
                </div>
            </div>

            
                            <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-white/50 mb-4">Khám phá</p>
                    <ul class="space-y-2.5">
                                                    <li>
                                <a href="/du-an"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Dự án
                                </a>
                            </li>
                                                    <li>
                                <a href="/so-cap"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Bán sơ cấp
                                </a>
                            </li>
                                                    <li>
                                <a href="/thu-cap"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Bán thứ cấp
                                </a>
                            </li>
                                                    <li>
                                <a href="/leasing/estate-for-rent"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Cho thuê
                                </a>
                            </li>
                                            </ul>
                </div>
                            <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-white/50 mb-4">Công ty</p>
                    <ul class="space-y-2.5">
                                                    <li>
                                <a href="/ve-chung-toi"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Về chúng tôi
                                </a>
                            </li>
                                                    <li>
                                <a href="/blog"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Tin tức
                                </a>
                            </li>
                                                    <li>
                                <a href="/lien-he"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Liên hệ
                                </a>
                            </li>
                                                    <li>
                                <a href="/cau-hoi-thuong-gap"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Câu hỏi thường gặp
                                </a>
                            </li>
                                            </ul>
                </div>
                            <div>
                    <p class="text-xs font-bold uppercase tracking-widest text-white/50 mb-4">Pháp lý</p>
                    <ul class="space-y-2.5">
                                                    <li>
                                <a href="/dieu-khoan"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Điều khoản sử dụng
                                </a>
                            </li>
                                                    <li>
                                <a href="/chinh-sach-quyen-rieng-tu"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Chính sách quyền riêng tư
                                </a>
                            </li>
                                                    <li>
                                <a href="/mien-tru-trach-nhiem"
                                   class="text-sm text-white/70 hover:text-white transition-colors duration-150 leading-snug">
                                    Miễn trừ trách nhiệm
                                </a>
                            </li>
                                            </ul>
                </div>
                    </div>
    </div>

    
    <div class="border-t border-white/8">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-5 flex flex-col sm:flex-row items-center justify-between gap-4">
            <p class="text-xs text-white/45">&copy; 2026 Bản quyền thuộc về Vinhomes Online. Mọi quyền được bảo lưu.</p>
            <div class="flex items-center gap-5">
                                    <a href="#" class="text-xs text-white/55 hover:text-white transition-colors duration-150">
                        Facebook
                    </a>
                                    <a href="#" class="text-xs text-white/55 hover:text-white transition-colors duration-150">
                        YouTube
                    </a>
                                    <a href="#" class="text-xs text-white/55 hover:text-white transition-colors duration-150">
                        Zalo
                    </a>
                            </div>
        </div>
    </div>

    
    <div class="border-t border-white/5 bg-black/20">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-4">
            <p class="text-[11px] leading-relaxed text-white/30">Thông tin trên website chỉ mang tính tham khảo, không phải là cam kết pháp lý.</p>
        </div>
    </div>
</footer>

    </body>
</html>
