
document.addEventListener("DOMContentLoaded", () => {

    const movimentoReduzido = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    // Entrada da página
    if (!movimentoReduzido) {
        document.body.classList.add("pagina-entrando");
    }

    // Prepara a saída dos links internos
    document.querySelectorAll("a[href]").forEach((link) => {

        link.addEventListener("click", (evento) => {

            if (
                movimentoReduzido ||
                evento.ctrlKey ||
                evento.shiftKey ||
                evento.altKey ||
                evento.metaKey ||
                evento.button !== 0 ||
                link.target === "_blank" ||
                link.hasAttribute("download") ||
                link.hasAttribute("data-sem-transicao")
            ) {
                return;
            }

            const href = link.getAttribute("href");

            if (
                !href ||
                href.startsWith("#") ||
                href.startsWith("javascript:")
            ) {
                return;
            }

            const destino = new URL(link.href, window.location.href);

            if (
                destino.origin !== window.location.origin ||
                destino.href === window.location.href
            ) {
                return;
            }

            evento.preventDefault();

            document.body.classList.remove("pagina-entrando");
            document.body.classList.add("pagina-saindo");

            setTimeout(() => {
                window.location.href = destino.href;
            }, 1000);

        });

    });

});
