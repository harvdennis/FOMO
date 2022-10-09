import React, { useState } from 'react'
import { Rating } from 'react-simple-star-rating'



export const Compdynamic = (props) => {
  const [rating, setRating] = useState(0) // initial rating value


  const handleRating = (rate: number) => {
    setRating(rate)
  }

 return (
    <div>
      <Rating
                    onClick={handleRating}
                    transition
                    ratingValue={rating}
                    size={50}
                    showTooltip
                    allowHalfIcon
                    fillColorArray={['#f17a45', '#f19745', '#f1a545', '#f1b345', '#f1d045']} 

                  />
                  <p>{rating/20}</p>
    
   
    </div>
  )
}