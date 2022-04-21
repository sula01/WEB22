import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VacancylistComponent } from './vacancylist.component';

describe('VacancylistComponent', () => {
  let component: VacancylistComponent;
  let fixture: ComponentFixture<VacancylistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VacancylistComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VacancylistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
