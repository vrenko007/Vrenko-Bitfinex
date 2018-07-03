import { Component, ViewChild, AfterViewInit, OnInit, OnDestroy} from '@angular/core';

import { jqxChartComponent } from '../../../node_modules/jqwidgets-scripts/jqwidgets-ts/angular_jqxchart';
import { DataService } from '../data/data.service';

@Component({
  selector: 'app-btc',
  templateUrl: './btc.component.html',
  styleUrls: ['./btc.component.css']
})
export class BTCComponent implements AfterViewInit, OnInit, OnDestroy {

  constructor(private dataService:DataService){

  }

  @ViewChild('BTCChart') myChart: jqxChartComponent;

  ngOnInit() {
  }

  ngAfterViewInit(): void {
    let data = this.myChart.source();
    
    const myObserver = {
      next: x => {
        var time: Date;
        var value: number;

        if(typeof(x) === 'object'){
          time = new Date(x['bitfinex_timestamp']*1000);
          value = x['bitfinex_price'];
        }
        else{
          let array = JSON.parse(x);
          time = new Date(array[3]*1000);
          value = array[4];
        }
        
        data.push({ timestamp: time, value: value });
        while(data.length > 20){
          data.shift();
        }
        this.myChart.update();
      },
      error: err => console.error('Observer got an error: ' + err),
      complete: () => console.log('Observer got a complete notification'),
    };
    this.dataService.getMessage().subscribe(myObserver);
    this.dataService.sendMessage("join","BTCUSD");
  }

  ngOnDestroy(): void {

    this.dataService.sendMessage("leave", "BTCUSD");

  }

  padding: any = { left: 5, top: 5, right: 5, bottom: 5 };

  titlePadding: any = { left: 0, top: 0, right: 0, bottom: 10 };

  xAxis: any =
  {
      dataField: 'timestamp',
      type: 'basic',
      unitInterval: 1,
      formatFunction: (value: any) => {
          return jqx.dataFormat.formatdate(value, 'hh:mm:ss', 'en-us');
      },
      labels: { angle: -45, offset: { x: -17, y: 0 } }
  };

  valueAxis: any =
  {
      title: { text: 'Price' },
      labels: { horizontalAlignment: 'right' }
  };

  seriesGroups: any[] =
  [
      {
          type: 'line',
          columnsGapPercent: 50,
          alignEndPointsWithIntervals: true,
          valueAxis:
          {
              title: { text: 'Price' }
          },
          series: [
              { dataField: 'value',
               displayText: 'value',
               opacity: 1,
               lineWidth: 2,
               symbolType: 'circle',
               fillColorSymbolSelected: 'white',
               symbolSize: 4,
               formatSettings: { decimalPlaces: 5 } }
          ]
      }
  ];
}