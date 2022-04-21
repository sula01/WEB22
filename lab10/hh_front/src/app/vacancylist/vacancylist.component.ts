import { Component, OnInit } from '@angular/core';
import {Company, Vacancy} from "../models";
import {CompanyServiceService} from "../company-service.service";
import {ActivatedRoute} from "@angular/router";
import {Location} from "@angular/common";
import {NONE_TYPE} from "@angular/compiler";

@Component({
  selector: 'app-vacancylist',
  templateUrl: './vacancylist.component.html',
  styleUrls: ['./vacancylist.component.css']
})
export class VacancylistComponent implements OnInit {
  vacancies_list:Vacancy[] = []
  // @ts-ignore
  companies: Company;
  constructor(private companyService:CompanyServiceService, private route: ActivatedRoute,
              private location: Location) { }

  ngOnInit(): void {
    this.getVac()
  }
  getVac(){
    this.route.paramMap.subscribe((params) => {
      // @ts-ignore
      const id = +params.get('id');

      this.companyService.getVacancies(id).subscribe((data) => {
        this.companies = data;
        this.vacancies_list = data['vacancy']
        console.log(data)
        console.log(data['vacancy'])
        console.log(this.vacancies_list)
      });
    });
  }


}
