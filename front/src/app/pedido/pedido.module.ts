import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PedidoFormComponent } from './pedido-form/pedido-form.component';
import { FormsModule } from '@angular/forms'

@NgModule({
  declarations: [PedidoFormComponent],
  imports: [
    CommonModule,
    FormsModule
  ],
  exports: [
    PedidoFormComponent,
  ]
})
export class PedidoModule { }
