import React, { Component } from 'react';
import '../css/task-board.css';

class TaskBoard extends Component {
    state = {  }
    componentDidMount()
    {
        console.log(this.props.tasks)
    }
    render() { 
        return (  
            <div style={{marginLeft:this.props.first && 10}} className="container">
            <div style={{backgroundColor:this.props.bgc}} className="head">
            <span className="title"><b>{this.props.title}</b></span><span className="num">{this.props.tasks.length}</span>
            </div>
            <div className="board">
            {this.props.tasks.map(task=><div className="task"><span style={{marginLeft:10}}>{task}</span><span style={{marginLeft:95}}><img src={require('../images/slingshot-options.png')} alt=""/></span></div>)}
            </div>
            </div>
        );
    }
}
 
export default TaskBoard;