import React, { Component } from 'react';
import '../css/slinger.css';
import axios from 'axios';

class Slinger extends Component {
    state = {windowHeight:window.innerHeight,windowWidth:window.innerWidth,collapsed:true,history:"",command:""}
    componentDidMount()
    {

        window.addEventListener("resize", this.handleResize);
    }
    barClick = () =>
    {
        const collapsed = !this.state.collapsed;
        this.setState({collapsed});
    }
    handleSubmit = (e) =>
    {
        e.preventDefault();
        const time = new Date().toLocaleTimeString();
        const text = e.target.value;
        axios.post("http://localhost:8080/predictions/lstm_topic",{command:text},{headers:{'Content-Type':'application/json'}}).then((response) => {
            const topic = response.data.Topic;
            const action = response.data.Action;
            const identifier = "NLP-user-command-app"
            const command = `😊  ${topic} ${identifier} successfully moved to ${action}`;
            const newhistory = this.state.history + command + ' ' + '\n' + time + '\n';
            this.setState({history:newhistory,command:""});
            this.props.updateProjects({name:identifier,status:action})

          }, (error) => {
            const command = '🙁  Something went wrong with the server';
            const newhistory = this.state.history + command + ' ' + '\n' + time + '\n';
            this.setState({history:newhistory,command:""})
          });
          

    }
    handleChange = (e) =>
    {
        const newvalue = e.target.value;
        this.setState({command:newvalue});
    }
    render() { 
        return ( 
            <React.Fragment>
            {this.state.collapsed && 
            <div onClick={this.barClick} className="slinger">
            <p className="label">Slinger<span style={{marginLeft:170}}><i class="fas fa-magic"></i></span></p>
            </div>
            }   
            {!this.state.collapsed && 
            <div className="expanded">
            <div onClick={this.barClick} className="header"><p className="label">Slinger<span style={{marginLeft:170}}><i class="far fa-window-minimize"></i></span></p></div>
            <textarea value = {this.state.history} className = "history" readOnly></textarea>
            <input value = {this.state.command} onChange={e => this.handleChange(e)} onKeyPress={event => {
                if (event.key === 'Enter') {
                  this.handleSubmit(event)
                }
              }} style={{height:50,width:300,border:'1px solid lightgrey',display:'block',borderTop:'none',marginTop:0}} type="text" placeholder="Enter a command..."></input>
            </div>
            }     
            </React.Fragment>
        );
    }
}
 
export default Slinger;