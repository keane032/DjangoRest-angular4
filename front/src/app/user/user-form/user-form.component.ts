import { Component, OnInit } from '@angular/core';
import {User} from '../../model/user.model';
import { UserService } from 'src/app/services/user.service';

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

  onSubmit(){
    this.userService.create(this.user).subscribe(
      (res:any) => {
          console.log(res)
      }  
    );
  }


}
