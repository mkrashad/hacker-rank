function regexVar() {
  /*
   * Declare a RegExp object variable named 're'
   * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
   */
  var str = "abcda"
  var patt1 = /aeiou+/g; 

  var result = str.match(patt1);
  var r = patt1.test(str)
  console.log(r);
}

regexVar()