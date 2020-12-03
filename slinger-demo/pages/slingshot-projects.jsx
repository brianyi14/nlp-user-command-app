import React, { Component } from 'react';
import '../css/slingshot-projects.css';

class Projects extends Component {
    state = {windowHeight:window.innerHeight,windowWidth:window.innerWidth,projects:this.props.projects,colorcode:{'On Target':' rgb(100,186,109)','At Risk':'rgb(252,182,35)','Danger':'rgb(237,79,81)','Completed':'rgb(116,136,244)'}}
    componentDidMount()
    {
        window.addEventListener("resize", this.handleResize);
    }
    
    render() { 
        return ( 
            <div style={{backgroundColor:'#EDEFF5',position:'absolute',left:60,top:60,width:this.state.windowWidth-60,height:this.state.windowHeight-60}}>
            <p className="title">Projects</p>
            <hr style={{marginLeft:45,marginRight:45,marginBottom:0}}></hr>
            <table style={{marginLeft:45}}>
            <tr style={{marginLeft:10}}>
            <th style={{width:680,height:35}}><span style={{marginLeft:10}}>Name</span></th>
            <th>Status</th>
            <th style={{width:100}}>Blocked</th>
            <th style={{width:100}}>Overdue</th>
            <th style={{width:45}}>Completed</th>
            <th></th>
            </tr>
            {this.state.projects.map((project => {return <tr style={{borderTop:'2px solid #EDEFF5'}}>
                <td className="name">{project.name}</td>
                <td><span className="status" style={{backgroundColor:this.state.colorcode[project.status]}}>{project.status}</span></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td><img src={require('../images/slingshot-options.png')} alt=""/></td></tr>}))}
            </table>
            </div>
        );
    }
}
 
export default Projects;