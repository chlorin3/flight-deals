# flight-deals
<table>
  <tr>
    <td>This app uses the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city.</td>
    <td><img src="https://github.com/chlorin3/flight-deals/blob/master/iataCodes.gif" width="50%" height="50%"/></td>
  </tr>
  <tr>
    <td>Then it uses the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.</td>
    <td></td>
  </tr>
  <tr>
    <td>If the price is lower than the lowest price listed in the Google Sheet then it sends an SMS to your own number with the Twilio API or sends emails to your customers
      who signed up to your club.</td>
    <td><img src="https://github.com/chlorin3/flight-deals/blob/master/customers.gif" width="100%" height="100%"/></td>
  </tr>
  <tr>
    <td>The SMS/email includes the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.</td>
    <td><img src="https://github.com/chlorin3/flight-deals/blob/master/Gmail.jpg" width="50%" height="50%"/>
    <img src="https://github.com/chlorin3/flight-deals/blob/master/sms.jpg" width="50%" height="50%"/>
    </td>
  </tr>
</table>