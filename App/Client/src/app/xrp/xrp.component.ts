import { Component, ViewChild, AfterViewInit, OnInit, O } from '@angular/core';

import { jqxChartComponent } from '../../../node_modules/jqwidgets-scripts/jqwidgets-ts/angular_jqxchart';
import { DataService } from '../data/data.service';


@Component({
  selector: 'app-xrp',
  templateUrl: './xrp.component.html',
  styleUrls: ['./xrp.component.css']
})
export class XRPComponent implements AfterViewInit, OnInit {

  constructor(private dataService:DataService){

  }

    @ViewChild('myChart') myChart: jqxChartComponent;

    ngOnInit() {
        this.generateChartData();
    }

    ngAfterViewInit(): void {
        let data = this.myChart.source();
        const myObserver = {
          next: x => 
          data.push({ timestamp: x.time, value: Math.max(100, (Math.random() * 1000) % max) }),
          error: err => console.error('Observer got an error: ' + err),
          complete: () => console.log('Observer got a complete notification'),
        };
        this.dataService.getMessage().subscribe(myObserver);



        let timer = setInterval(() => {
          let max = 800;
          if (data.length >= 60)
              data.splice(0, 1);
          let timestamp = new Date();
          timestamp.setSeconds(timestamp.getSeconds());
          timestamp.setMilliseconds(0);
          data.push({ timestamp: timestamp, value: Math.max(100, (Math.random() * 1000) % max) });
          this.myChart.update();
      }, 1000);
    }

    data: any[] = [];

    padding: any = { left: 5, top: 5, right: 5, bottom: 5 };

    titlePadding: any = { left: 0, top: 0, right: 0, bottom: 10 };

    xAxis: any =
    {
        dataField: 'timestamp',
        type: 'date',
        baseUnit: 'second',
        unitInterval: 5,
        formatFunction: (value: any) => {
            return jqx.dataFormat.formatdate(value, 'hh:mm:ss', 'en-us');
        },
        gridLines: { step: 2 },
        valuesOnTicks: true,
        labels: { angle: -45, offset: { x: -17, y: 0 } }
    };

    valueAxis: any =
    {
        minValue: 0,
        maxValue: 1000,
        title: { text: 'Index Value' },
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
                minValue: 0,
                maxValue: 1000,
                title: { text: 'Index Value' }
            },
            series: [
                { dataField: 'value', displayText: 'value', opacity: 1, lineWidth: 2, symbolType: 'circle', fillColorSymbolSelected: 'white', symbolSize: 4 }
            ]
        }
    ];

    generateChartData = () => {
        let max = 800;
        let timestamp = new Date();
        for (let i = 0; i < 60; i++) {
            timestamp.setMilliseconds(0);
            timestamp.setSeconds(timestamp.getSeconds() - 1);
            this.data.push({ timestamp: new Date(timestamp.valueOf()), value: Math.max(100, (Math.random() * 1000) % max) });
        }
        this.data = this.data.reverse();
    }

}