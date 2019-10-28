import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserFormComponent } from './user-form/user-form.component';
import {FormsModule} from '@angular/forms'
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [UserFormComponent],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule
  ],
  exports:[
    UserFormComponent
  ]
})
export class ClienteModule { }
