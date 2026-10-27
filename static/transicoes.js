
document.addEventListener("DOMContentLoaded", () => {

    // Anima a entrada da página
    document.body.classList.add("pagina-entrando");

    // Prepara as transições dos links internos
    document.querySelectorAll("a[href]").forEach((link) => {

        link.addEventListener("click", (evento) => {

            // Ignora atalhos, outras abas e cliques especiais
            if (
                evento.ctrlKey ||
                evento.shiftKey ||
                evento.altKey ||
                evento.metaKey ||
                evento.button !== 0 ||
                link.target === "_blank" ||
                link.hasAttribute("download")
            ) {
                return;
            }

            const destino = new URL(link.href, window.location.href);

            // Não anima links externos, âncoras ou a mesma página
            if (
                destino.origin !== window.location.origin ||
                destino.pathname === window.location.pathname &&
                destino.search === window.location.search &&
                destino.hash
            ) {
                return;
            }

            // Deixa o navegador cuidar de links especiais
            if (
                link.href.startsWith("javascript:") ||
                link.hasAttribute("data-sem-transicao")
            ) {
                return;
            }

            evento.preventDefault();

            document.body.classList.add("pagina-saindo");

            setTimeout(() => {
                window.location.href = destino.href;
            }, 200);

        });

    });

});
