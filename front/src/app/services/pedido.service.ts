import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Pedido } from '../model/pedido.model';


@Injectable({
  providedIn: 'root'
})
export class PedidoService {

  constructor(private http:HttpClient) { }

  create(pedido:Pedido){
    return this.http.post("http://localhost:8000/pedidos/",pedido);
  }

  get_processadores(){
    return this.http.get("http://localhost:8000/processador")
  }

  get_memorias(){
    return this.http.get("http://localhost:8000/memoria")
  }

  get_placamae(){
    return this.http.get("http://localhost:8000/placamae")
  }
  
}
