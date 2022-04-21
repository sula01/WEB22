import { Injectable } from '@angular/core';
import {HTTP_INTERCEPTORS, HttpClient, HttpClientModule} from '@angular/common/http';
import {Observable} from 'rxjs';
import {AuthToken, Company} from './models';
import { AppComponent } from './app.component';
@Injectable({
  providedIn: 'root'
})
export class CompanyServiceService {
  BASE_URl = 'http://127.0.0.1:8000/';
  constructor(private http:HttpClient) { }
  // @ts-ignore
  login(username, password): Observable<AuthToken> {
    return this.http.post<AuthToken>(`${this.BASE_URl}api/login/`, {
      username,
      password
    });
  }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URl}api/companies/`);
  }
  getVacancies(id:number): Observable<Company> {
    return this.http.get<Company>(`${this.BASE_URl}api/companies/${id}/vacancies/`);
  }
}
