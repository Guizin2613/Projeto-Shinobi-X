
document.addEventListener("DOMContentLoaded", () => {

    // Anima a entrada da página
    document.body.classList.add("pagina-entrando");

    // Verifica se o usuário prefere menos animações
    const movimentoReduzido = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    // Prepara as transições dos links
    document.querySelectorAll("a[href]").forEach((link) => {

        link.addEventListener("click", (evento) => {

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

            const href = link.getAttribute("href");

            if (
                link.hasAttribute("data-sem-transicao") ||
                !href ||
                href.startsWith("#") ||
                href.startsWith("javascript:")
            ) {
                return;
            }

            const destino = new URL(link.href, window.location.href);

            // Só anima a navegação dentro do próprio site
            if (destino.origin !== window.location.origin) {
                return;
            }

            // Não anima se o endereço já for o atual
            if (destino.href === window.location.href) {
                return;
            }

            // Respeita a preferência por movimento reduzido
            if (movimentoReduzido) {
                return;
            }

            evento.preventDefault();

            // Inicia a saída lateral
            document.body.classList.add("pagina-saindo");

            // Aguarda a animação terminar antes de navegar
            setTimeout(() => {
                window.location.href = destino.href;
            }, 1000);

        });

    });

});
