import React, { Component } from 'react';
import NavBar from '../components/top-nav';
import VerticalNav from '../components/left-nav';
import Projects from '../pages/slingshot-projects';
import Slinger from '../components/slinger';

class Website extends Component {
    state = {projects:[]}
    updateProjects = (status_update) =>
    {
        const projects = this.state.projects;
        const name = status_update.name;
        const update = status_update.status;
        const idx = projects.findIndex(p => p.name == name);
        if (idx === null)
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
    render() { 
        return (  
                <div>
                <NavBar/>
                <VerticalNav/>
                <Projects projects={this.state.projects}/>
                <Slinger addProject = {this.addProject} updateProjects={this.updateProjects}/>
                </div>
        );
    }
}
 
export default Website;