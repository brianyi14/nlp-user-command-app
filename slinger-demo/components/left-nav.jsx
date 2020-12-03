import React, { Component } from 'react';

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
            <img ref={ (button) => { this.project = button} }style={{marginLeft:(60-this.state.projectwidth)/2,marginTop:20}} src={require('../images/slingshot-projects.png')} alt=""/>
            <img style={{marginLeft:(60-this.state.projectwidth)/2,marginTop:20}} src={require('../images/slingshot-tasks.png')} alt=""/>
            </div>
        );
    }
}
 
export default VerticalNav;