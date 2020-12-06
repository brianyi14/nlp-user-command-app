import React, { Component } from 'react';
import {Link} from 'react-router-dom';
import '../css/left-nav.css';

class VerticalNav extends Component {
    state = {windowHeight:window.innerHeight,projectwidth:0}
    componentDidMount()
    {
        window.addEventListener("resize", this.handleResize);
        const projectwidth = this.project.clientWidth;
        this.setState({projectwidth})
    }
    render() { 
        return ( 
            <div style={{backgroundColor:'#3D498A',position:'absolute',left:0,top:60,width:60,height:this.state.windowHeight-60}}>
            <Link to="/"><img className="icon" ref={ (button) => { this.project = button} }style={{position:'absolute',left:(60-this.state.projectwidth)/2,top:20}} src={require('../images/slingshot-projects.png')} alt=""/></Link>
            <Link to="/Tasks"><img className="icon" style={{position:'absolute',left:(60-this.state.projectwidth)/2,top:60}} src={require('../images/slingshot-tasks.png')} alt=""/></Link>
            </div>
        );
    }
}
 
export default VerticalNav;