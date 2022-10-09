import { Comp } from './Comp';
import React, {useMemo} from 'react'



export const COLUMNS = [
  
     {
        Header: 'Course Ranking',
        accessor: 'courseRanking'
    },
        {
        Header: 'Course Name',
        accessor: 'courseName'
    },
        {
        Header: 'Difficulty Rating',
        accessor: 'difficultyRating',
        Cell: props => {
          return  <Comp rating={props.value}/>
        }



  },
        
        
    
        {
        Header: 'Credits',
        accessor: 'credits'
    }

]