import { Component, OnInit } from '@angular/core';
import {User} from '../../model/user.model';
import { UserService } from 'src/app/services/user.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})

export class UserFormComponent implements OnInit {

  user:User;

  constructor(private userService:UserService) {
    this.user = new User();
  }

  ngOnInit() {
  }

  onSubmit(form:NgForm){
    this.userService.create(this.user).subscribe(
      (res:any) => {
          alert("Usuario cadastrado :0 sue identificador " + res.id)
          form.reset()
      },
      (erro:any) => {
            alert("campo nome obrigatorio")
      }  
    );
  }


}
