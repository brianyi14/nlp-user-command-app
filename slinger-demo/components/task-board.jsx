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
            <div className="container">
            <div className="head">
            {this.props.title}
            </div>
            <div className="board">
            {this.props.tasks.map(task=><div className="task"><p>{task}</p></div>)}
            </div>
            </div>
        );
    }
}
 
export default TaskBoard;