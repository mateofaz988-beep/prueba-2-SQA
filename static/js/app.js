document.addEventListener('DOMContentLoaded', function() {
    const userCards = document.querySelectorAll('.user-card');
    
    userCards.forEach(card => {
        card.addEventListener('click', function(e) {
            if (!e.target.classList.contains('btn')) {
                const btn = this.querySelector('.btn');
                if (btn) {
                    window.location.href = btn.getAttribute('href');
                }
            }
        });
    });
});
