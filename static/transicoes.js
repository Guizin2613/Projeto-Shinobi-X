
document.addEventListener("DOMContentLoaded", () => {

    // Verifica se o usuário prefere menos animações
    const movimentoReduzido = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    // Se o navegador não oferece suporte, não interfere na navegação
    if (
        movimentoReduzido ||
        !document.startViewTransition
    ) {
        return;
    }

});
