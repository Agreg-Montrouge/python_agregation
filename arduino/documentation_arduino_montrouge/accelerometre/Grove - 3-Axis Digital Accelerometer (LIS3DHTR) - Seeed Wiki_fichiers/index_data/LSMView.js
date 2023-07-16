!function(e){function t(t){for(var i,a,u=t[0],c=t[1],s=t[2],l=0,f=[];l<u.length;l++)a=u[l],Object.prototype.hasOwnProperty.call(r,a)&&r[a]&&f.push(r[a][0]),r[a]=0;for(i in c)Object.prototype.hasOwnProperty.call(c,i)&&(e[i]=c[i]);for(d&&d(t);f.length;)f.shift()();return o.push.apply(o,s||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],i=!0,u=1;u<n.length;u++){var c=n[u];0!==r[c]&&(i=!1)}i&&(o.splice(t--,1),e=a(a.s=n[0]))}return e}var i={},r={27:0},o=[];function a(t){if(i[t])return i[t].exports;var n=i[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,a),n.l=!0,n.exports}a.m=e,a.c=i,a.d=function(e,t,n){a.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},a.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,t){if(1&t&&(e=a(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(a.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var i in e)a.d(n,i,function(t){return e[t]}.bind(null,i));return n},a.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return a.d(t,"a",t),t},a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},a.p="";var u=window.webpackJsonp=window.webpackJsonp||[],c=u.push.bind(u);u.push=t,u=u.slice();for(var s=0;s<u.length;s++)t(u[s]);var d=c;o.push([1060,2]),n()}({1060:function(e,t,n){e.exports=n(1061)},1061:function(e,t,n){"use strict";n.r(t);var i=n(32),r=n(9),o=n(208);function a(e){return(a="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function u(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}function c(e,t){return(c=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e})(e,t)}function s(e){var t=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}();return function(){var n,i=f(e);if(t){var r=f(this).constructor;n=Reflect.construct(i,arguments,r)}else n=i.apply(this,arguments);return d(this,n)}}function d(e,t){if(t&&("object"===a(t)||"function"==typeof t))return t;if(void 0!==t)throw new TypeError("Derived constructors may only return object or undefined");return l(e)}function l(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function f(e){return(f=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}var p=window.__APP__.createModule,h=Object(r.c)("data-layerstack-label",""),y=[{id:"5277e6a4-9e5f-4f54-951f-dc18cfeb7530",name:"Rigid-flex",supported:!1,check:function(e){return!0}},{id:"e3df2b86-5f1b-49ca-b266-d1ae57f0ba6f",name:"Impedance Profiles",supported:!1,check:function(e){return Array.isArray(e.stackup.impedanceProfiles)&&e.stackup.impedanceProfiles.length}},{id:"0a82ba33-e4d8-43f3-9c01-412dc26bdd5e",name:"Backdrill",supported:!1,check:function(e){return!0}}];e=p({type:"View",description:"LSM View module.",create:function(e){return new(function(e){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),Object.defineProperty(e,"prototype",{writable:!1}),t&&c(e,t)}(d,e);var t,n,r,a=s(d);function d(){var e,t,n,i;return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,d),e=a.call(this,{name:"LSMView",displayName:"Stackup",comment:"LSM View module",description:"LSM View module",order:3,dependencies:["lsm"]}),t=l(e),i=function(t){e.active&&(!t||82!==t.keyCode&&"KeyR"!==t.code||setTimeout((function(){return e.engine.resetView()}),1))},(n="onKeyUp")in t?Object.defineProperty(t,n,{value:i,enumerable:!0,configurable:!0,writable:!0}):t[n]=i,e.logger=window.__CORE__.createLogger("LSMView"),e.isHidden=!0,e.isTopView=!1,e.showWarning=!0,e.lockedPlugin="",e}return t=d,(n=[{key:"hidden",get:function(){return this.isHidden}},{key:"events",get:function(){return["LSMView:documentChanged","LSMView:didInit","LSMView:resetView","LSMView:shown","LSMView:hidden","LSMView:documentInfo","LSMView:features","LSMView:enableSelection"]}},{key:"hasControls",value:function(e){e.push({type:"select"}),e.push({type:"zoom"}),e.push({type:"pan"}),e.push({type:"reset"})}},{key:"setup",value:function(e){var t=this;return new Promise((function(n){t.Core=e,t.engine=t.Core.engines.LsmEngine;var r=e.response.metadata;if(t.engine){var a,u;t.isTopView="Camtastic"===r.projectTypeName;var c=t.isTopView&&(null===(a=e.response)||void 0===a||null===(u=a.storage)||void 0===u?void 0:u.files.some((function(e){return"Lsm"===e.fileType})));t.isHidden=!c,h&&"prod"!==h.toLowerCase()&&t.setBadges([Object(o.a)(h)]),window.addEventListener("keyup",t.onKeyUp),t.Core.bus.on("LsmEngine:didDocumentAttach",(function(e){t.active&&t.showWarning&&t.initWarning(),t.updateLoader(),t.Core.bus.emit("LSMView:documentChanged",e.documentId)})),t.Core.bus.on("LsmEngine:didDocumentAttachError",(function(e){var n=e.error;e.documentId,n.code===i.a.StoreExpired?t.updateLoader("error",n.message,"info-16","small"):t.updateLoader("error",n.message),t.Core.bus.emit("Document:open-error",{name:"LSM",message:n.message,error:n})})),t.Core.bus.on("LSMView:documentInfo",(function(e){var n;if(e){var i;if(e.id)i=t.engine.allDocuments.find((function(t){return t.pcbId===e.id}));else{var r=t.engine.activeDocumentIndex;i=t.engine.allDocuments[r]}if(i&&(e.id=i.pcbId,e.name=null!==(n=i.displayName)&&void 0!==n?n:i.name,i.stackup)){var o=i.stackup.stackup.stacks.find((function(e){return e.id===i.currentStackId}));o&&(e.id=i.pcbId,e.name=o.name,e.stackId=o.id)}}})),t.Core.bus.on("LSMView:resetView",(function(){return t.onResetView()})),t.Core.bus.on("LSMView:enableSelection",(function(e){t.engine.enableSelection(e)}))}n()}))}},{key:"activate",value:function(e){var t=this;this.logger.LogDebug("Activate LSM view"),this.div=e,this.active=!0,this.engine?this.engine.showView(e).then((function(n){return new Promise((function(n){t.Core.bus.emit("LSMView:shown",e),n()}))})).catch((function(e){return t.updateLoader("error",e.message)})):this.updateLoader("error","LSM engine has not found."),this.hideViews(),this.showWarning&&this.initWarning()}},{key:"deactivate",value:function(){this.logger.LogDebug("Deactivate LSM view"),this.active=!1,this.Core.bus.emit("Views:updatePadding",{top:0,right:0}),this.engine&&(this.engine.hideView(),this.Core.bus.emit("LSMView:hidden")),this.updateLoader(),this.restoreViews(),this.notification.close(),this.Core.bus.emit("LsmProperties:disable")}},{key:"lockPlugin",value:function(e){e!==this.lockedPlugin&&(this.lockedPlugin&&e?this.logger.LogWarn("Try to freeze panel [".concat(e,"] then the panel [").concat(this.lockedPlugin,"] is frozen")):this.lockedPlugin=null!=e?e:"")}},{key:"onResetView",value:function(){this.engine.resetView()}},{key:"updateLoader",value:function(e,t,n){var i=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"large";if(this.loader&&(this.loader.destroy(),this.loader=null),this.div&&e&&t){var r={message:t,type:e,size:i};n&&(r.icon=n),this.loader=window.__APP__.loader(this.div,r)}}},{key:"hideViews",value:function(){var e=this;this.isTopView||Object.keys(this.Core.views).forEach((function(t){e.Core.bus.emit("".concat(t,":updateInterface"),{hidden:"LSMView"!==t})})),this.Core.bus.emit("HelpPanel:updateInterface",{hidden:!0}),this.Core.bus.emit("LsmProperties:updateInterface",{hidden:!1})}},{key:"restoreViews",value:function(){var e=this;this.isTopView||Object.values(this.Core.views).forEach((function(t){var n,i;e.Core.bus.emit("".concat(null==t||null===(n=t.metaInfo)||void 0===n?void 0:n.name,":updateInterface"),{hidden:"LSMView"===(null==t||null===(i=t.metaInfo)||void 0===i?void 0:i.name)||(null==t?void 0:t.hidden)})})),this.Core.bus.emit("HelpPanel:updateInterface",{hidden:!1}),this.Core.bus.emit("LsmProperties:updateInterface",{hidden:!0})}},{key:"getWarningMessage",value:function(){var e=this.getFeatures();if(Array.isArray(e)&&e.length){var t="Note: The following features are not displayed in the Web UI: ";return e.forEach((function(e,n){t+=n?", ".concat(e.name):e.name})),t}return""}},{key:"getFeatures",value:function(){var e=this.engine.activeDocumentIndex,t=this.engine.allDocuments[e];if(null!=t&&t.stackup)return y.filter((function(e){return t.stackup.featureSet.some((function(n){return n.id===e.id&&e.check(t.stackup)}))}))}},{key:"initWarning",value:function(){var e=this,t=this.getWarningMessage();this.notification||(this.notification=window.__APP__.notification(document.querySelector("#viewer-app"))),t&&this.notification.update({text:t})&&this.notification.open(),this.notification.onClose((function(){e.showWarning=!1}))}}])&&u(t.prototype,n),r&&u(t,r),Object.defineProperty(t,"prototype",{writable:!1}),d}(e))}});window.__CORE__&&window.__CORE__.addModule(e)}});