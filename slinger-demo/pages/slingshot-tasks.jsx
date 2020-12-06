import React, { Component } from 'react';
import TaskBoard from '../components/task-board';

class Tasks extends Component {
    state = {windowHeight:window.innerHeight,windowWidth:window.innerWidth,boards:{0:'todo',1:'inprogress',2:'inreview',3:'blocked',4:'completed'},boardtitles:['To Do','In Progress','In Review','Blocked','Completed']}
    componentDidMount()
    {
        window.addEventListener("resize", this.handleResize);
    }
    
    render() { 
        return ( 
            <div style={{backgroundColor:'#EDEFF5',position:'absolute',overflow:'scroll',left:60,top:60,width:this.state.windowWidth-60,height:this.state.windowHeight-60}}>
            <table >
            <tr>
            {this.state.boardtitles.map((board,idx) => <td style={{backgroundColor:'#EDEFF5'}}><TaskBoard tasks={this.props[this.state.boards[idx]]} title={board}/></td>)}
            </tr>
            </table>
            </div>
        );
    }
}
 
export default Tasks;