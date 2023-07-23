Vue.component('daily-calendar', {
    props: [
        'year',
        'month',
        'day'
    ],
    data: function () {
        return {
            daysOfWeek: [
                "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"
            ],
            months: [
                "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "OCT", "SEP", "OCT", "NOV", "DEC"
            ]
        }
    },
    methods: {
        date: function () {
            return new Date(this.year, this.month - 1, this.day + 1);
        },
        dayOfWeek: function () {
            const day = this.date().getDay();
            const index = (day < 2 ? day + 5 : day - 2);
            return this.daysOfWeek[index];
        },
        weekNumber: function () {
            const d = this.date();
            var dayNum = d.getUTCDay() || 7;
            d.setUTCDate(d.getUTCDate() + 4 - dayNum);
            var yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
            return Math.ceil((((d - yearStart) / 86400000) + 1) / 7)
        }
    },
    template:
        '<table style="width: 100%; padding: 0; margin: 0">' +
        '    <tr>' +
        '        <td style="width: 0px">' +
        '            <div>' +
        '                <div style=" font-size: 8px; width: 20px; height: 10px; text-align: center; background-color: black; vertical-align: middle; color: lightgray; padding-top: 2px">' +
        '                    {{ months[month - 1] }}' +
        '                </div>' +
        '                <div style="width: 20px; height: 20px; text-align: center; background-color: crimson; vertical-align: middle">' +
        '                    <div style="color: white; font-size: 12px; height: 20px; padding-top: 4px">' +
        '                        {{ day }}' +
        '                    </div>' +
        '                </div>' +
        '            </div>' +
        '        </td>' +
        '        <td style="width: 400px;font-size: 10px; ">' +
        '            <div style="color: lightgrey; display: block; padding: 4px; margin-bottom: 2px; height: 8px; padding-top: 0">' +
        '                WEEK {{ weekNumber() }}' +
        '            </div>' +
        '            <div v-for="day in daysOfWeek"' +
        '                 :style="\'display: inline-block; padding: 4px; \' + (dayOfWeek() === day ? \'color: white; background-color: crimson\' : \'\') ">' +
        '                {{ day }}' +
        '            </div>' +
        '        </td>' +
        '    </tr>' +
        '</table>'

});

