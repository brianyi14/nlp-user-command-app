import React, { Component } from 'react';
import NavBar from '../components/top-nav';
import VerticalNav from '../components/left-nav';
import Projects from '../pages/slingshot-projects';
import Tasks from '../pages/slingshot-tasks';
import Slinger from '../components/slinger';
import {Route,Switch,Redirect} from 'react-router-dom';

class Website extends Component {
    state = {projects:[],todo:['Market Research'],inprogress:[],inreview:[],blocked:[],completed:[],tasks:{'Market Research':'todo'},actions:{'To Do':'todo','In Progress':'inprogress','In Review':'inreview','Blocked':'blocked','Completed':'completed'}}
    updateProjects = (status_update) =>
    {
        const projects = this.state.projects;
        const name = status_update.name;
        const update = status_update.status;
        const idx = projects.findIndex(p => p.name == name);
        if (idx === -1)
        {
            return 0;
        }
        else
        {
            projects[idx].status = update;
            this.setState({projects});
            return 1;
        }
    }
    addProject = (project) =>
    {
        const name = project.name;
        const status = 'On Target';
        const newproject ={name,status}
        const projects = this.state.projects;
        projects.push(newproject);
        this.setState({projects})
    }
    addTask = (taskname) =>
    {
        const newtodo = this.state.todo;
        newtodo.push(taskname);
        const newtasks = this.state.tasks
        newtasks[taskname] = 'todo'
        this.setState({todo:newtodo,tasks:newtasks});
    }
    updateTasks = (status_update) =>
    {
        const tasks = this.state.tasks;
        const name = status_update.name;
        const update = status_update.status;
        if (name in tasks === true)
        {
            const oldstatus = tasks[name];
            const oldtasks = this.state[oldstatus];
            const idx = oldtasks.indexOf(name)
            oldtasks.splice(idx,1);
            const newstatus = this.state.actions[update];
            const newtasks = this.state[newstatus];
            newtasks.push(name);
            tasks[name] = newstatus;
            this.setState({tasks,[oldstatus]:oldtasks,[newstatus]:newtasks});
            return 1;
        }
        else
        {
            return 0;
        }
    }
    render() { 
        return (  
                <div>
                <NavBar/>
                <VerticalNav/>
                <Switch>
                <Route path='/Tasks' render={(props)=><Tasks {...props} todo={this.state.todo} inprogress={this.state.inprogress} inreview={this.state.inreview} blocked={this.state.blocked} completed={this.state.completed}/>}/>
                <Route path='/' render={(props)=><Projects {...props} projects={this.state.projects}/>}/>
                </Switch>
                <Slinger addTask = {this.addTask} updateTasks={this.updateTasks} addProject = {this.addProject} updateProjects={this.updateProjects}/>
                
                </div>
        );
    }
}
 
export default Website;