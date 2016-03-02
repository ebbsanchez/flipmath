lastScrollTop = undefined
console.log 'coffee go'
lastScrollTop = 0

mq = window.matchMedia('(max-width: 736px)')
console.log("mq: " + mq.matches)
if !mq.matches
  $(window).scroll ->
    st = undefined
    st = $(this).scrollTop()
    console.log 'hi:', st
    if st > lastScrollTop and st > 0
      $('nav').fadeOut()
    else if st < lastScrollTop or st <= 0
      $('nav').fadeIn()
    lastScrollTop = st
    return
