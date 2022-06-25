window.onload = () => {
    let q, range, stars
    const input_rating = $('#rating')
    const low_price = $('#low_price')
    const high_price = $('#high_price')
    const q_search = $('#q-search')
    const search_btn = $('#search-btn')

    //amm session
    const ammStars = sessionStorage.getItem('amm-stars')
    const ammRange = sessionStorage.getItem('amm-range')
    const ammQ = sessionStorage.getItem('amm-q')
    if (ammStars) {
        stars = Number(ammStars)
        input_rating.val(stars);
    }

    search_btn.on('click', () => {
        // stars
        stars = stars ? stars : 4
        input_rating.val(stars);
        sessionStorage.setItem('amm-stars', stars)
        // stars end
        //range
        if (range) {
            const array = range.split(',')
            if (array && array.length) {
                const l = array[0]
                const h = array[1]
                low_price.val(h || 0)
                high_price.val(l || 0)
                sessionStorage.setItem('amm-range', range)
            }
        }
        //range end
        //qsearch
        if (q) {
            alert(value)
            if (value && q) {
                sessionStorage.setItem('amm-q', q)
            }
        }
        //qsearch end
    })

    q_search.on('change', (e) => {
        q = e.target.value
    })

    $('.range-slider').jRange({
        from: 0,
        to: 100,
        step: 1,
        format: '%s',
        width: 300,
        showLabels: true,
        isRange: true,
        onstatechange: (e) => {
            range = e
            console.log(range, 'range')
        }
    });
    setTimeout(() => {
        if (ammRange) {
            range = ammRange
            $('.range-slider').jRange('setValue', range || '10, 20');
        }
    }, 100)

    console.warn(ammQ, 'ammQ')
    if (ammQ) {
        console.warn(ammQ, 'ammQ111111')
        q = ammQ
        q_search.val(ammQ)
    }

    $("#my-rating").starRating({
        initialRating: Number(ammStars) || 4,
        strokeColor: '#de003f',
        strokeWidth: 10,
        starSize: 15,
        disableAfterRate: false,
        useFullStars: true,
        callback: (currentRating) => {
            stars = currentRating
            console.log(stars, 'current rating')
            // make a server call here
        }
    });
}
