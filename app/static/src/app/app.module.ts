import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import 'hammerjs';
import { RouterModule, Routes } from '@angular/router';


const appRoutes: Routes = [
    {
        path      : '**',
        //redirectTo: '/PATH-TO-HOME',
        pathMatch: 'full'
    },

];

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(appRoutes,{useHash:true}), // Allows angular to reload components in browser.
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
