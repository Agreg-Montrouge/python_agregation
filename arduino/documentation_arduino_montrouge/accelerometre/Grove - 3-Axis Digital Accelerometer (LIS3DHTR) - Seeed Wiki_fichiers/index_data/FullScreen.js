!function(e){function n(n){for(var r,u,c=n[0],i=n[1],a=n[2],f=0,d=[];f<c.length;f++)u=c[f],Object.prototype.hasOwnProperty.call(l,u)&&l[u]&&d.push(l[u][0]),l[u]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);for(s&&s(n);d.length;)d.shift()();return o.push.apply(o,a||[]),t()}function t(){for(var e,n=0;n<o.length;n++){for(var t=o[n],r=!0,c=1;c<t.length;c++){var i=t[c];0!==l[i]&&(r=!1)}r&&(o.splice(n--,1),e=u(u.s=t[0]))}return e}var r={},l={22:0},o=[];function u(n){if(r[n])return r[n].exports;var t=r[n]={i:n,l:!1,exports:{}};return e[n].call(t.exports,t,t.exports,u),t.l=!0,t.exports}u.m=e,u.c=r,u.d=function(e,n,t){u.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:t})},u.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},u.t=function(e,n){if(1&n&&(e=u(e)),8&n)return e;if(4&n&&"object"==typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(u.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var r in e)u.d(t,r,function(n){return e[n]}.bind(null,r));return t},u.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return u.d(n,"a",n),n},u.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},u.p="";var c=window.webpackJsonp=window.webpackJsonp||[],i=c.push.bind(c);c.push=n,c=c.slice();for(var a=0;a<c.length;a++)n(c[a]);var s=i;o.push([1039,2]),t()}({1039:function(e,n,t){e.exports=t(1040)},1040:function(e,n,t){"use strict";t.r(n);var r=t(9);function l(e){return(l="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function o(e,n){for(var t=0;t<n.length;t++){var r=n[t];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}function u(e,n){return(u=Object.setPrototypeOf||function(e,n){return e.__proto__=n,e})(e,n)}function c(e){var n=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}();return function(){var t,r=s(e);if(n){var l=s(this).constructor;t=Reflect.construct(r,arguments,l)}else t=r.apply(this,arguments);return i(this,t)}}function i(e,n){if(n&&("object"===l(n)||"function"==typeof n))return n;if(void 0!==n)throw new TypeError("Derived constructors may only return object or undefined");return a(e)}function a(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function s(e){return(s=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function f(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}var d=window.__CORE__,p=window.__APP__.createModule,v=window.__APP__,y=v.analytics,m=v.parentEvents,b=v.utils.getIcon,h="true"===Object(r.c)("data-outside-fullscreen",!1),w="true"===Object(r.c)("data-force-outside-fullscreen",!1);e=p({type:"Plugin",name:"FullScreen",description:"FullScreen",create:function(e){return new(function(e){!function(e,n){if("function"!=typeof n&&null!==n)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(n&&n.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),Object.defineProperty(e,"prototype",{writable:!1}),n&&u(e,n)}(i,e);var n,t,r,l=c(i);function i(){var e;return function(e,n){if(!(e instanceof n))throw new TypeError("Cannot call a class as a function")}(this,i),f(a(e=l.call(this,{name:"FullScreen",displayIcon:b("viewer-fullscreen-16","fullscreen-16"),comment:"FullScreen",description:"FullScreen",order:5,hint:"Switch full screen mode",preventModalClose:!0,disableActiveBtnState:!0})),"screenExpanded",!1),f(a(e),"changeScreenExpanded",(function(){e.screenExpanded?(e.screenExpanded=!1,document.removeEventListener(e.fullScreenEvent,e.changeScreenExpanded),d.bus.emit("FullScreen:disable")):e.screenExpanded=!0})),e.fullScreenEvent=e.getFullScreenEvent(),e}return n=i,(t=[{key:"hidden",get:function(){return this.isHidden}},{key:"setup",value:function(){return this.fullScreenEvent||h||(this.isHidden=!0,d.bus.emit("Fullscreen:updateInterface",{hidden:!0})),Promise.resolve()}},{key:"activate",value:function(){if(d.bus.emit("FullScreen:updateInterface",{displayIcon:b("viewer-fullscreen-cancel-16","fullscreen-cancel-16")}),y.dispatchClickEvent("Fullscreen",{action:"Fullscreen"}),w)return this.emitFullscreenEventToParentWindow(!0);this.fullScreenEvent?(this.isIpad()&&this.addIpadClass(),this.toggleFullScreen(),document.addEventListener(this.fullScreenEvent,this.changeScreenExpanded)):h&&this.emitFullscreenEventToParentWindow(!0)}},{key:"deactivate",value:function(){return d.bus.emit("FullScreen:updateInterface",{displayIcon:b("viewer-fullscreen-16","fullscreen-16")}),w?this.emitFullscreenEventToParentWindow(!1):(this.isIpad()&&this.removeIpadClass(),this.fullScreenEvent?this.screenExpanded&&this.toggleFullScreen():void this.emitFullscreenEventToParentWindow(!1))}},{key:"getFullScreenEvent",value:function(){var e=window.document.documentElement,n={requestFullscreen:"fullscreenchange",webkitRequestFullScreen:"webkitfullscreenchange",mozRequestFullScreen:"mozfullscreenchange",msRequestFullscreen:"MSFullscreenChange"};for(var t in n)if(e[t])return n[t];return null}},{key:"toggleFullScreen",value:function(){var e=window.document,n=e.documentElement,t=n.requestFullscreen||n.mozRequestFullScreen||n.webkitRequestFullScreen||n.msRequestFullscreen,r=e.exitFullscreen||e.mozCancelFullScreen||e.webkitExitFullscreen||e.msExitFullscreen;e.fullscreenElement||e.mozFullScreenElement||e.webkitFullscreenElement||e.msFullscreenElement?r.call(e):t.call(n)}},{key:"isIpad",value:function(){return!!(navigator.userAgent.match(/(iPad)/)||"MacIntel"===navigator.platform&&void 0!==navigator.standalone)}},{key:"addIpadClass",value:function(){document.querySelector(".app").classList.add("app_ipad-fullscreen")}},{key:"removeIpadClass",value:function(){document.querySelector(".app").classList.remove("app_ipad-fullscreen")}},{key:"emitFullscreenEventToParentWindow",value:function(e){m.emit("viewer:fullscreen",e)}}])&&o(n.prototype,t),r&&o(n,r),Object.defineProperty(n,"prototype",{writable:!1}),i}(e))}});window.__CORE__&&window.__CORE__.addModule(e)}});