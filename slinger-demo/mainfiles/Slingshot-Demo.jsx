import React, { Component } from 'react';
import NavBar from '../components/top-nav';
import VerticalNav from '../components/left-nav';
import Projects from '../pages/slingshot-projects';
import Slinger from '../components/slinger';

class Website extends Component {
    state = {projects:[{name: 'NLP-user-command-app',status:'On Target'},{name:'NLP-user-command-app',status:'On Target'}]}
    updateProjects = (status_update) =>
    {
        const projects = this.state.projects;
        const name = status_update.name;
        const update = status_update.status;
        const idx = projects.findIndex(p => p.name == name);
        projects[idx].status = update;
        this.setState({projects});
    }
    render() { 
        return (  
                <div>
                <NavBar/>
                <VerticalNav/>
                <Projects projects={this.state.projects}/>
                <Slinger updateProjects={this.updateProjects}/>
                </div>
        );
    }
}
 
export default Website;