import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  changeColor = 'success';
  colors: string[] = ['#000000', '#db0f0f', '#0fbf0f', '#35a3e8', '#FFFFFF'];
  color: string[] = ['yellow', 'blue', 'red', '', '#FFFFFF'];
  clr = '#D3D3D3';
  currentColor: string = this.colors[1];

  constructor() {
    this.changeColor = 'my-special-color';

  }
  changeColors(cl){
    console.log(cl);
    if ( cl === 'r'){
      console.log('red');
      this.clr = '#f53d3d' ;
    }
    if ( cl === 'g'){
      console.log('green');

      this.clr = '#32db64' ;
     }
    if ( cl === 'b' ){
      console.log('red');
      this.clr = '#488aff' ;
     }

  }
  switchColor(index: number) {
    this.currentColor = this.colors[index];
  }
}
