class Rectangle {
  constructor(w, h) {
    this.w = w;
    this.h = h;
  }
}


  /*
  *  Write code that adds an 'area' method to the Rectangle class' prototype
  
  */
Rectangle.prototype.area = function() {
    return this.h * this.w
}


class Square extends Rectangle {
  constructor(s) {
    super(s, s)
  }
}

/*
* Create a Square class that inherits from Rectangle and implement its class constructor
*/
