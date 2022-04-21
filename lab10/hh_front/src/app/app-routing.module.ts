import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {CompanyComponent} from "./company/company.component";
import {VacancylistComponent} from "./vacancylist/vacancylist.component";
const routes: Routes = [
  {path: '', component:CompanyComponent},
  {path: 'vacancies/:id', component:VacancylistComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
