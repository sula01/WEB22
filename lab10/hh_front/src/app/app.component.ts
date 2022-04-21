import { Component } from '@angular/core';
import {CompanyServiceService} from "./company-service.service";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'hh_front';

  logged = false;
  username = '';
  password = '';
  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }
  constructor(private companyService: CompanyServiceService) {
  }

  login() {
    this.companyService.login(this.username, this.password).subscribe((data) => {

      localStorage.setItem('token', data.token);

      this.logged = true;
      this.username = '';
      this.password = '';
    });
  }

  logout() {
    this.logged = false;
    localStorage.removeItem('token');
  }
}
