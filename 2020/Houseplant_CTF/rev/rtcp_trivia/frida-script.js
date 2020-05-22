/*  Android ssl certificate pinning bypass script for various methods
    by Maurizio Siddu

    Run with:
    frida -U -f [APP_ID] -l frida-script.js --no-pause
*/

Java.perform(function () {
    var nx = Java.use('nx');
    nx.a.overload('java.lang.String').implementation = function(x) {
      console.log(x);
      var tmp = this.a.call(this, x);
      console.log(JSON.stringify(tmp));
      return tmp;
    }
    nx.b.implementation = function(x) {
      console.log(x);
      var tmp = this.b.call(this, x);
      console.log(JSON.stringify(tmp));
      return tmp;
    }

    /*var strbuild = Java.use('java.lang.StringBuilder');
    strbuild.append.overload('java.lang.String').implementation = function(x) {
      console.log("Val: " + x);
      strbuild.append.call(x);
    }*/
//java.security.spec.AlgorithmParameterSpec
    /*var Cipher = Java.use('javax.crypto.Cipher');
    Cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec').implementation = function(x, y, z) {
      console.log(x)
      console.log(JSON.stringify(y))
      console.log(JSON.stringify(z))
    }*/
});
