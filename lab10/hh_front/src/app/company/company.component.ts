import { Component, OnInit } from '@angular/core';
import {Company} from "../models";
import {CompanyServiceService} from "../company-service.service";
@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {
  companies: Company[] = [];

  constructor(private companyService:CompanyServiceService) { }

  ngOnInit(): void {
    this.getCompanies();

  }
  getCompanies(){
    this.companyService.getCompanies().subscribe((data) => {
      this.companies = data;
      console.log(data)
      console.log(this.companies)
    });
  }
}
