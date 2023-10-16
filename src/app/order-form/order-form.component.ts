import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
//import { NgForm } from '@angular/forms';
import {FormsModule} from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-order-form',
  templateUrl: './order-form.component.html',
  styleUrls: ['./order-form.component.css'],
})


export class OrderFormComponent {

  constructor(private http: HttpClient) {}


  submitOrder(orderDetails: any) {
    // Call the backend API to send email
    //orderDetails.name = "nandan"
    console.log(("order details = " + orderDetails.name));
    this.http.post('https://l685zpq80g.execute-api.us-east-2.amazonaws.com/prod/sendemail', orderDetails).subscribe(
      response => {
        console.log('Email sent successfully!', response);
        alert('Order submitted successfully! ' +
	       'Please bring the racket to 14 Angelica Ct, Princeton, NJ 08540. ' +
	       'Contact 732 438 1427 with any questions </div>');
      },
      error => {
        console.error('Failed to send email', error);
        alert('Failed to submit order. Please try again later.');
      }
    );
  }
}

