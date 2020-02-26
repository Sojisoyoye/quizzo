import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { Quiz } from './quiz/quiz.model';
import { QuizService } from './quiz/quiz.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'client';
  quizListSub: Subscription;
  quizList: Quiz[];

  constructor(private quizService: QuizService) {}

  ngOnInit() {
    this.quizListSub = this.quizService.getData().subscribe(res => {
      this.quizList = res;
    },
    console.error
    )
  }

  ngOnDestroy() {
    this.quizListSub.unsubscribe();
  }
}
