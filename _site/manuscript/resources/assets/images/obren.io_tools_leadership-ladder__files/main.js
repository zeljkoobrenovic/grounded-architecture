window.onload = function () {
    vueApp = new Vue({
        el: '#app',
        created: function () {
            let id = findGetParameter("id");
            if (id) {
                this.id = id;
            } else {
                this.id = "";
            }
            this.loadDataFromStorage();

            const self = this;
            setTimeout(function () {
                self.update();
            }, 3000)
        },
        data: function () {
            return {
                id: "",
                json: "",
                message: "",
                showDetails: false,
                defaultCodData: {
                    projects: [
                        {
                            name: "A",
                            durationInWeeks: 2,
                            revenuePerWeek: 5000,
                            revenueFromWeek: 1
                        },
                        {
                            name: "B",
                            durationInWeeks: 4,
                            revenuePerWeek: 15000,
                            revenueFromWeek: 1
                        },
                        {
                            name: "C",
                            durationInWeeks: 8,
                            revenuePerWeek: 20000,
                            revenueFromWeek: 1
                        }
                    ]
                },
                codData: {}
            }
        },
        methods: {
            addProject: function () {
                this.codData.projects.push({
                    name: "Project",
                    durationInWeeks: 2,
                    revenuePerWeek: 0,
                    revenueFromWeek: 1
                });
            },
            removeProject: function (project) {
                const index = this.codData.projects.indexOf(project);
                if (index > -1) {
                    this.codData.projects.splice(index, 1);
                }
            },
            loadDataFromStorage: function () {
                if (window.localStorage) {
                    try {
                        let json = window.localStorage.getItem(this.fullId());
                        if (json) {
                            this.json = json;
                            let data = JSON.parse(json);
                            if (data) {
                                this.codData = data;
                            } else {
                                this.reset();
                            }
                        } else {
                            this.reset();
                        }
                    } catch (err) {
                        console.log(err);
                    }
                } else {
                    this.reset();
                }
            },
            weeks: function (completionScenarios) {
                const weeks = [];

                for (let i = 0; i < completionScenarios.totalDurationInWeeks + 1; i++) {
                    weeks.push(i + 1);
                }


                return weeks;
            },
            weeksProject: function (project) {
                const weeks = [];

                for (let i = 0; i < project.durationInWeeks; i++) {
                    weeks.push(i + 1);
                }


                return weeks;
            },
            updateCostOfDelayPerWeek: function (scenario, totalDurationInWeeks) {
                scenario.totalCostOfDelay = 0;
                scenario.revenuePerWeekEstimate = [];
                scenario.maxRevenue = 1;
                scenario.maxCost = 1;
                for (let i = 0; i < totalDurationInWeeks; i++) {
                    scenario.revenuePerWeekEstimate.push(0);
                }
                for (let p = 0; p < scenario.projects.length; p++) {
                    const project = scenario.projects[p];
                    project.revenuePerWeekEstimate = [];
                    project.costOfDelayPerWeek = [];

                    for (let pcd = 0; pcd < scenario.costOfDelayPerWeek.length + parseInt(project.durationInWeeks); pcd++) {
                        let week = pcd + 1;
                        let projectRevenue = week >= project.revenueFromWeek ? project.revenuePerWeek : 0;
                        project.costOfDelayPerWeek.push(projectRevenue);
                        project.revenuePerWeekEstimate.push(0);
                    }

                    for (let pcd = project.costOfDelayPerWeek.length; pcd < totalDurationInWeeks; pcd++) {
                        project.revenuePerWeekEstimate.push(project.revenuePerWeek);
                        scenario.revenuePerWeekEstimate[pcd] += parseInt(project.revenuePerWeek);
                    }


                    for (let w = 0; w < project.durationInWeeks; w++) {
                        let costPerWeek = 0;
                        let week = scenario.costOfDelayPerWeek.length + 1;
                        for (let pRest = p; pRest < scenario.projects.length; pRest++) {
                            let projectRevenue = week >= scenario.projects[pRest].revenueFromWeek ? scenario.projects[pRest].revenuePerWeek : 0;
                            costPerWeek += parseInt(projectRevenue);
                        }
                        scenario.costOfDelayPerWeek.push(costPerWeek);
                        scenario.totalCostOfDelay += costPerWeek;
                    }
                }

                scenario.costOfDelayPerWeek.forEach(cost => scenario.maxCost = Math.max(scenario.maxCost, cost))

                scenario.costOfDelayPerWeek.push(0);
                let maxProjectRevenue = 0;
                scenario.projects.forEach(p => maxProjectRevenue += parseInt(p.revenuePerWeek));
                scenario.revenuePerWeekEstimate.push(maxProjectRevenue);
                scenario.maxRevenue = maxProjectRevenue;
            },
            numberWithCommas: function (x) {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            },
            getNullScenario: function (completionScenarios, projects) {
                let scenario0 = {
                    name: "All Projects Together",
                    projects: [{
                        name: "All Projects",
                        durationInWeeks: completionScenarios.totalDurationInWeeks,
                        revenuePerWeek: 0,
                        revenueFromWeek: 1
                    }],
                    costOfDelayPerWeek: [],
                    revenuePerWeekEstimate: [],
                    totalCostOfDelay: 0,
                    maxRevenue: 1,
                    maxCost: 1
                }

                for (let week = 1; week <= completionScenarios.totalDurationInWeeks; week++) {
                    let costOfDelayPerWeek = 0;
                    let revenuePerWeekEstimate = 0;
                    projects.forEach(project => {
                        let costOfDelayInWeek = week < project.revenueFromWeek ? 0 : project.revenuePerWeek;
                        costOfDelayPerWeek += parseInt(costOfDelayInWeek);
                    });
                    scenario0.revenuePerWeekEstimate.push(0);
                    scenario0.costOfDelayPerWeek.push(costOfDelayPerWeek);
                    scenario0.totalCostOfDelay += costOfDelayPerWeek;
                    scenario0.maxCost = Math.max(scenario0.maxCost, costOfDelayPerWeek);
                    scenario0.maxRevenue = Math.max(scenario0.maxRevenue, costOfDelayPerWeek);
                }
                scenario0.revenuePerWeekEstimate.push(scenario0.maxRevenue);
                scenario0.costOfDelayPerWeek.push(0);
                console.log(scenario0);
                return scenario0;
            }, completionScenarios: function () {
                const completionScenarios = {
                    scenarios: [],
                    totalDurationInWeeks: 0
                };

                let projects = this.codData.projects.filter(project => project.durationInWeeks > 0);
                projects.forEach(project => completionScenarios.totalDurationInWeeks += parseInt(project.durationInWeeks));

                let scenario0 = this.getNullScenario(completionScenarios, projects);
                completionScenarios.scenarios.push(scenario0);

                let scenario1 = {
                    name: "Shortest First",
                    projects: JSON.parse(JSON.stringify(projects)).sort((a, b) => {
                        if (a.durationInWeeks === b.durationInWeeks) {
                            return a.revenuePerWeek - b.revenuePerWeek;
                        }
                        return a.durationInWeeks - b.durationInWeeks;
                    }),
                    costOfDelayPerWeek: [],
                    totalCostOfDelay: 0
                }

                this.updateCostOfDelayPerWeek(scenario1, completionScenarios.totalDurationInWeeks);
                completionScenarios.scenarios.push(scenario1);

                let scenario2 = {
                    name: "Most Valuable First",
                    projects: JSON.parse(JSON.stringify(projects)).sort((a, b) => {
                        if (b.revenuePerWeek === a.revenuePerWeek) {
                            return b.durationInWeeks - a.durationInWeeks;
                        }
                        return b.revenuePerWeek - a.revenuePerWeek;
                    }),
                    costOfDelayPerWeek: [],
                    totalCostOfDelay: 0
                };
                this.updateCostOfDelayPerWeek(scenario2, completionScenarios.totalDurationInWeeks);
                completionScenarios.scenarios.push(scenario2);

                let scenario3 = {
                    name: "Highest CD3 Score First",
                    projects: JSON.parse(JSON.stringify(projects)).sort((a, b) => {
                        return Math.round(b.revenuePerWeek / b.durationInWeeks) - Math.round(a.revenuePerWeek / a.durationInWeeks);
                    }),
                    costOfDelayPerWeek: [],
                    totalCostOfDelay: 0
                };
                this.updateCostOfDelayPerWeek(scenario3, completionScenarios.totalDurationInWeeks);
                completionScenarios.scenarios.push(scenario3);

                return completionScenarios;
            },
            fullId: function () {
                return "cost_of_delay" + (this.id.length > 0 ? "_" + this.id : "");
            },
            reset: function () {
                this.codData = JSON.parse(JSON.stringify(this.defaultCodData));
                this.update();
            },
            update: function () {
                const self = this;
                if (window.localStorage) {
                    const json = JSON.stringify(this.codData);
                    if (json !== this.json) {
                        this.json = json;
                        window.localStorage.setItem(self.fullId(), json);
                        self.message = "SAVED."
                    }
                    setTimeout(function () {
                        self.message = "";
                        self.update();
                    }, 2000);
                }
            }
        }
    });
}
