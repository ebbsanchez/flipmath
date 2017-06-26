lastScrollTop = undefined
console.log 'coffee go'
lastScrollTop = 0

mq = window.matchMedia('(max-width: 736px)')
console.log("mq: " + mq.matches)
if !mq.matches
  $(window).scroll ->
    st = undefined
    st = $(this).scrollTop()
    console.log 'scrollTop:', st
    if st > lastScrollTop and st > 0
      $('nav').fadeOut()
    else if st < lastScrollTop or st <= 0
      $('nav').fadeIn()
    lastScrollTop = st
    return

touch_menu = ->
  $('#menu-button').click (e) ->
    if $('nav').css('display') == 'none'
      $('nav').css 'display', 'block'
      console.log $('nav').css('display') == 'block'
      return
    else
      return $('nav').css('display', 'none')
    
  

$(document).ready ->
  touch_menu()
  return