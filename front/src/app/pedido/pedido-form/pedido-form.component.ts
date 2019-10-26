import { Component, OnInit } from '@angular/core';
import { Pedido } from 'src/app/model/pedido.model';
import { PedidoService } from 'src/app/services/pedido.service';


@Component({
  selector: 'app-pedido-form',
  templateUrl: './pedido-form.component.html',
  styleUrls: ['./pedido-form.component.css']
})
export class PedidoFormComponent implements OnInit {

  pedido:Pedido;
  processadores:[];
  memorias:[];
  placas_mae:[];

  constructor(private pedidoService:PedidoService) { 
    this.pedido = new Pedido();
  }

  ngOnInit() {
    this.get_data()
    // this.pedido.memorias = [1];
  }
  onSubmit(){
    this.pedidoService.create(this.pedido).subscribe(
      (res:any) => {
          console.log(res)
      }
    )
  }

  get_data(){
    this.pedidoService.get_processadores().subscribe(
      (res:any)=>{
        this.processadores=res
        console.log(res)
      }
    )
    this.pedidoService.get_placamae().subscribe(
      (res:any)=>{
        this.placas_mae=res
      }
    )
    this.pedidoService.get_memorias().subscribe(
      (res:any)=>{
        this.memorias=res
      }
    )
  }

}
