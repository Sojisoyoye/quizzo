import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { API_URL } from '../env';
import { Quiz } from './quiz.model';



@Injectable({
  providedIn: 'root'
})
export class QuizService {

  constructor(private http: HttpClient) { }

  private handleError(operation: String) {
    return (err: any) => {
      let errMsg = `error in ${operation}() retrieving ${API_URL}`;
      console.log(`${errMsg}:`, err)
      if (err instanceof HttpErrorResponse) {
        console.log(`status: ${err.status}, ${err.statusText}`);
        errMsg = `status: ${err.status}, ${err.statusText}`;
      }
      return Observable.throw(errMsg);
    }
  }

  public getData(): Observable<Quiz[]> {
    return this.http
      .get<Quiz[]>(`${API_URL}/quiz`)
      .pipe(
        tap(data => console.log('server data:', data)),
        catchError(this.handleError('getData'))
      );
  }
}
