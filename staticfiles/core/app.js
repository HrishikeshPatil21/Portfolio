(function(){
  var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
  var el=document.getElementById('typed'),roles=(el.dataset.roles||el.textContent).split(',').map(function(x){return x.trim()}).filter(Boolean),ri=0,ci=0,del=false;
  function type(){var w=roles[ri];ci+=del?-1:1;el.textContent=w.slice(0,ci)||'\u00a0';
    var t=del?40:80;if(!del&&ci===w.length){del=true;t=1400}else if(del&&ci===0){del=false;ri=(ri+1)%roles.length;t=300}setTimeout(type,t)}
  if(!reduce)type();
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;e.target.classList.add('in');
    var n=e.target.querySelector('[data-n]');if(n)count(n);io.unobserve(e.target)})},{threshold:.2});
  document.querySelectorAll('.rv').forEach(function(x){io.observe(x)});
  function count(n){var to=+n.dataset.n,d=(n.dataset.n.split('.')[1]||'').length;if(reduce){n.textContent=to.toFixed(d);return}
    var s=performance.now();(function f(t){var p=Math.min((t-s)/1200,1);n.textContent=(to*p).toFixed(d);if(p<1)requestAnimationFrame(f)})(s)}
  if(!reduce)document.querySelectorAll('.tilt').forEach(function(c){
    c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
      c.style.transform='rotateY('+x*8+'deg) rotateX('+(-y*8)+'deg) translateY(-4px)'});
    c.addEventListener('pointerleave',function(){c.style.transform=''})});
  var root=document.documentElement;
  document.getElementById('theme').addEventListener('click',function(){
    var dark=root.dataset.theme?root.dataset.theme==='dark':matchMedia('(prefers-color-scheme:dark)').matches;root.dataset.theme=dark?'light':'dark'});
})();
